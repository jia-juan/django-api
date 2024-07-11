from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from demo.models.order import Order
from demo.serializers.order import OrderModelSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = [IsAuthenticated]


class StatusOptionsViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        status_choices = Order._meta.get_field('status').choices
        options = [{'value': choice[0], 'display_name': choice[1]} for choice in status_choices]
        return Response(options)