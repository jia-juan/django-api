from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from demo.models.customer import Customer
from demo.serializers.customer import CustomerModelSerializer


class CustomerReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerModelSerializer
    permission_classes = [IsAuthenticated]
