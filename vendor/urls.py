from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ShopViewSet, ProductCategoryViewSet, ProductColorViewSet, ProductViewSet, CartViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'product-colors', ProductColorViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
