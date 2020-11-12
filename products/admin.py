from django.contrib import admin
from .models import Category, Product, Wishlist, OrderItem, Order
# Register your models here.



admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(OrderItem)
admin.site.register(Order)
