from django.contrib import admin
from demo.models.product import Product
from demo.models.customer import Customer
from demo.models.order import Order
from demo.models.order_item import OrderItem

admin.site.register(Product)
admin.site.register(Customer)
# admin.site.register(Order)
# admin.site.register(OrderItem)
