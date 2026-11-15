from rest_framework import serializers
from .models import CartItem,Cart


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_price = serializers.DecimalField(source="product.price",max_digits=10, decimal_places=2, read_only=True)
    subtotal = serializers.DecimalField(source="subtotal", max_digits=12, decimal_places=2, read_only=True)


    class Meta:
        model = CartItem
        fields = ["id", "product", "product_name", "price", "image","quantity", "subtotal"]
    def validate(self, attrs):
        product = attrs.get("product") or self.instance.product

        default_qty = self.instance.quantity if self.instance else 1
        quantity = attrs.get("quantity", default_qty)

        if not product.is_active:
            raise serializers.ValidationError("This product is not available.")

        if quantity > product.stock:
            raise serializers.ValidationError(f"Only {product.stock} in stock.")
        return attrs

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True
    )

    class Meta:
        model = Cart
        fields = ["id", "items", "total"]