from rest_framework import serializers

from productapi.models import ProductCategory, Product, Product_brands, Exclusive_promotions, Trending_Items, \
    Feature_Products


class ProductCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class Product_brandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_brands
        fields = '__all__'


class Feature_ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feature_Products
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    # feature_name = Feature_ProductsSerializers(source='feature_products_name', many=True, required=False, read_only=True)
    # feature = serializers.Feature_ProductsSerializers(source='feature_products_name.all')
    # objectives = serializers.RelatedField(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        # fields = [
        #           'prod_category',
        #           'prod_brand',
        #           'name',
        #           'product_desc',
        #           'product_price',
        #           'product_quantity',
        #           'created_at',
        #           'updated_at',
        #           ]


class Exclusive_promotionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exclusive_promotions
        fields = '__all__'


class Trending_ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trending_Items
        fields = '__all__'
