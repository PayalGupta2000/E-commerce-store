from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'quantity', 'total_price', 'created_at']
        read_only_fields = ['total_price', 'created_at']

    def validate(self, data):
        product = data['product']
        quantity = data['quantity']
        
        if product.stock < quantity:
            raise serializers.ValidationError("Not enough stock available for this product.")
        elif  not quantity or int(quantity) <= 0:
            raise serializers.ValidationError('Quantity must be a positive integer.')

        
        return data

    def create(self, validated_data):
        # Reduce the product's stock when the order is placed
        product = validated_data['product']
        product.stock -= validated_data['quantity']
        product.save()
        
        # Create the order
        order = Order.objects.create(**validated_data)
        return order