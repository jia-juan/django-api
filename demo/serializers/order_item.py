from rest_framework import serializers
from demo.models.order_item import OrderItem


class OrderItemModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'
