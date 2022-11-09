from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from productapi.models import ProductCategory, Product, Product_brands, Exclusive_promotions, Trending_Items, \
    Feature_Products, MyStripeModel, StripeSubscription
from productapi.Serializers import ProductCategorySerializers, ProductSerializers, Product_brandsSerializer, \
    Exclusive_promotionsSerializers, Trending_ItemsSerializers, Feature_ProductsSerializers, MyStripeModelSerializers, \
    StripeSubscriptionSerializers
# Create your views here.


class ProductCategoryViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProductCategorySerializers
    queryset = ProductCategory.objects.all()


class Product_brandsViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = Product_brandsSerializer
    queryset = Product_brands.objects.all()

    def get_queryset(self):
        query = self.queryset
        category = self.request.query_params.get("category")
        if category:
            query = query.filter(prod_category=category)
        return query
    # def update(self, request, *args, **kwargs):


class ProductViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializers
    queryset = Product.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = {
                'products': serializer.data,
                'feature_projects': Feature_ProductsSerializers(Feature_Products.objects.filter(), many=True).data
            }

            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)

        data = {
            'products': serializer.data,
            'feature_projects': ProductSerializers(Product.objects.filter(), many=True)
        }

        return Response(data)


class Exclusive_promotionsViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = Exclusive_promotionsSerializers
    queryset = Exclusive_promotions.objects.all()


class Trending_ItemsViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = Trending_ItemsSerializers
    queryset = Trending_Items.objects.all()


class Future_ProductsViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = Feature_ProductsSerializers
    queryset = Feature_Products.objects.all()


class MyStripeModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = MyStripeModelSerializers
    queryset = MyStripeModel.objects.all()


class StripeSubscriptionViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = StripeSubscriptionSerializers
    queryset = StripeSubscription.objects.all()



# def get_queryset(self):
#     query = self.queryset
#     cat = self.request.query_params.get("category")
#     if cat:
#         query = query.filter(prod_category=cat)
#     return query

# def list(self, request, *args, **kwargs):
#     serializer = self.serializer_class(self.queryset)
#     if cat:
#         query = self.queryset.filter(prod_category=cat)
#         serializer = self.serializer_class(query, many=True)
#         return Response(serializer.data)
#     return Response(serializer.data)
