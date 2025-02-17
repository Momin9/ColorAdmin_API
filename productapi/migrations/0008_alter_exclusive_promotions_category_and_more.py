# Generated by Django 4.1.3 on 2022-11-07 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapi', '0007_future_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exclusive_promotions',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Exclusive_promotions_product_name', to='productapi.productcategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exclusive_promotions',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='future_products',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Future_products_name', to='productapi.productcategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='future_products',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trending_items',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trending_items',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Trending_Items_product_name', to='productapi.product'),
            preserve_default=False,
        ),
    ]
