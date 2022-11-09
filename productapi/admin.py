from django.contrib import admin

from productapi.models import Product, ProductCategory, Product_brands, Exclusive_promotions, Trending_Items, \
    Feature_Products, StripeSubscription, MyStripeModel

# Register your models here.


admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Product_brands)
admin.site.register(Exclusive_promotions)
admin.site.register(Trending_Items)
admin.site.register(Feature_Products)
admin.site.register(StripeSubscription)
admin.site.register(MyStripeModel)












# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ["id", "name"]
#
# @admin.register(ProductCategory)
# class ProductCategoryAdmin(admin.ModelAdmin):
#     list
