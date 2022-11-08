# Generated by Django 4.1.3 on 2022-11-07 08:20

from django.db import migrations, models
import django.db.models.deletion
import productapi.models


class Migration(migrations.Migration):

    dependencies = [
        ('productapi', '0003_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.TextField(default=1, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='Category name'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Product_brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prod_category', models.ForeignKey(on_delete=models.SET(productapi.models.get_default_product_category), related_name='category', to='productapi.productcategory')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='prod_brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='productapi.product_brands'),
        ),
    ]