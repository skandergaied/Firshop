from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.decorators import action
from .models import Order,OrderItem
from django.db import transaction
from django.shortcuts import get_object_or_404
from products.models import Product


SHIPPING_FIELDS = ["full_name", "phone", "street", "city", "country"]


# Create your views here.

class OrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        orders = Order.objects.filter(user=request.user).prefetch_related("items")
        return Response(OrderSerializer(orders, many=True).data)

    def retrieve(self, request, pk=None):
        orders = Order.objects.filter(user=request.user)
        order = get_object_or_404(orders, pk=pk)
        return Response(OrderSerializer(order).data)


    @action(detail=False, methods=["post"], url_path="checkout")

    def checkout(self, request):

        missing = [f for f in SHIPPING_FIELDS if not request.data.get(f)]
        if missing:
            return Response({"detail": f"Missing: {', '.join(missing)}"}, status=400)

        cart =Cart.objects.get(user=request.user).first()
        if not cart or not cart.items.exists():
            return Response({"detail": "Your cart is empty."}, status=400)

        with transaction.atomic():
            order = Order.objects.create(
                user=request.user,
                total_price=0,
                full_name=request.data["full_name"],
                phone=request.data["phone"],
                street=request.data["street"],
                city=request.data["city"],
                postal_code=request.data.get("postal_code", ""),
                country=request.data["country"],
            )
        total = 0
        for item in cart.items.select_related("product"):

            product = Product.objects.select_for_update().get(pk=item.product_id)

            if not product.is_active:
                raise_error = f"{product.name} is not available."
                transaction.set_rollback(True)
                return Response({"detail": raise_error}, status=400)
            if item.quantity > product.stock:
                transaction.set_rollback(True)
                return Response(
                    {"detail": f"Only {product.stock} of {product.name} in stock."},
                    status=400,
                )
            OrderItem.objects.create(
            order=order,
            product=product,
            product_name=product.name,
            quantity=item.quantity,
            price=product.price,
           )
            product.stock -= item.quantity
            product.save()
            total += product.price * item.quantity

        order.total_price = total
        order.save()
        cart.items.all().delete()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)




