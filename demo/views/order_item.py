from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from demo.models.order import Order
from demo.serializers.order import OrderModelSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = [IsAuthenticated]
