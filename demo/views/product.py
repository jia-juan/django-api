from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from demo.models.product import Product
from demo.serializers.product import ProductModelSerializer


class ProductReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [IsAuthenticated]
