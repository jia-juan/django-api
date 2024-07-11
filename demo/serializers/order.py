from rest_framework import serializers
from demo.models.order import Order


class OrderModelSerializer(serializers.ModelSerializer):
    customer_username = serializers.CharField(source='customer.user.username', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
