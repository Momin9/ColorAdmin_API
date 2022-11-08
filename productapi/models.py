from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _
from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(_('Category name'), max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


def get_default_product_category():
    return ProductCategory.objects.get_or_create(name='Others')[0]


class Product_brands(models.Model):
    prod_category = models.ForeignKey(
        ProductCategory, related_name="category", on_delete=models.SET(get_default_product_category))
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    prod_category = models.ForeignKey(
        ProductCategory, related_name="product_list", on_delete=models.SET(get_default_product_category))
    prod_brand = models.ForeignKey(Product_brands, related_name="product_brand", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    product_desc = models.TextField(_('Description'))
    product_price = models.DecimalField(decimal_places=2, max_digits=10)
    product_quantity = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Trending_Items(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='Trending_Items_product_name')
    name = models.CharField(max_length=255)
    trend_prod_desc = models.TextField(_('Description'), blank=True)
    trend_prod_price = models.DecimalField(decimal_places=2, max_digits=10)
    trend_prod_discount_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class Exclusive_promotions(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,
                                 related_name='Exclusive_promotions_product_name')
    name = models.CharField(max_length=255)
    excl_prod_desc = models.TextField(_('Description'), blank=True)
    excl_prod_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class Feature_Products(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,
                                 related_name='Future_products_name')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='feature_products_name')
    name = models.CharField(max_length=255)
    feature_prod_desc = models.TextField(_('Description'), blank=True)
    feature_prod_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name
