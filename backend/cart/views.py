from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer


def get_cart(user):  # step 14
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]  # step 13

    # view cart
    def list(self, request):
        cart = get_cart(request.user)
        return Response(CartSerializer(cart).data)

    # add item (step 16)
    @action(detail=False, methods=["post"], url_path="add")
    def add_item(self, request):
        cart = get_cart(request.user)
        serializer = CartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.validated_data["product"]
        quantity = serializer.validated_data["quantity"]

        item, created = CartItem.objects.get_or_create(
            cart=cart, product=product, defaults={"quantity": quantity}
        )
        if not created:
            new_qty = item.quantity + quantity
            if new_qty > product.stock:
                return Response(
                    {"detail": f"Only {product.stock} in stock."}, status=400
                )
            item.quantity = new_qty
            item.save()
        return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)

    # change quantity
    @action(detail=False, methods=["patch"], url_path=r"items/(?P<item_id>\d+)")
    def update_item(self, request, item_id=None):
        cart = get_cart(request.user)
        item = get_object_or_404(cart.items, pk=item_id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(CartSerializer(cart).data)

    # remove item
    @action(detail=False, methods=["delete"], url_path=r"items/(?P<item_id>\d+)/remove")
    def remove_item(self, request, item_id=None):
        cart = get_cart(request.user)
        cart.items.filter(pk=item_id).delete()
        return Response(CartSerializer(cart).data)

    # clear cart
    @action(detail=False, methods=["delete"], url_path="clear")
    def clear_cart(self, request):
        cart = get_cart(request.user)
        cart.items.all().delete()
        return Response(CartSerializer(cart).data)