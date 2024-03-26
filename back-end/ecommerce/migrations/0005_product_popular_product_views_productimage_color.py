# Generated by Django 4.1.5 on 2023-02-20 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_remove_product_specifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='popular',
            field=models.BooleanField(default=False, verbose_name='პოპულარული'),
        ),
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='ნახვები'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='color',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ფერი'),
        ),
    ]
