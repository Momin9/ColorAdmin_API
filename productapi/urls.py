from rest_framework.routers import DefaultRouter
from django.urls import path, include

from productapi.views import ProductCategoryViewSet, ProductViewSet, Product_brandsViewSet, Exclusive_promotionsViewSet, \
    Trending_ItemsViewSet, Future_ProductsViewSet

router = DefaultRouter()
router.register(r'productCategory', ProductCategoryViewSet, basename="ProductCategoryViewSet")
router.register(r'product', ProductViewSet, basename="product")
router.register(r'product_brands', Product_brandsViewSet, basename="Product_brandsViewSet")
router.register(r'exclusive_promotions', Exclusive_promotionsViewSet, basename="Exclusive_promotionsViewSet")
router.register(r'trending_Items', Trending_ItemsViewSet, basename="Trending_ItemsViewSet")
router.register(r'future_productsViewSet', Future_ProductsViewSet, basename="Future_ProductsViewSet")


urlpatterns = [
    path("", include(router.urls)),

]

