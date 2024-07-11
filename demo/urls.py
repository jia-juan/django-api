from django.urls import path, include
from rest_framework.routers import DefaultRouter
from demo.views.order import OrderViewSet, StatusOptionsViewSet
from demo.views.order_item import OrderItemViewSet
from demo.views.customer import CustomerReadOnlyViewSet
from demo.views.product import ProductReadOnlyViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
# router.register(r'order_items', OrderItemViewSet)  # fixme 不能用底線
router.register(r'customer', CustomerReadOnlyViewSet)
router.register(r'product', ProductReadOnlyViewSet)

router.register(r'order-status', StatusOptionsViewSet, basename='order-status')

urlpatterns = [
    path('', include(router.urls)),
]