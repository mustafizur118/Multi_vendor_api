from django.contrib import admin
from .models import User, Shop, ProductCategory, ProductColor, Product, Cart, Order

admin.site.register(User)
admin.site.register(Shop)
admin.site.register(ProductCategory)
admin.site.register(ProductColor)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)

