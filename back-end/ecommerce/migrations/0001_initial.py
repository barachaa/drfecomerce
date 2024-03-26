# Generated by Django 4.1.5 on 2023-02-15 09:56

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='სახელი')),
            ],
            options={
                'verbose_name': 'კატეგორია',
                'verbose_name_plural': 'კატეგორიები',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='აქტიურია')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ფასდაკლება')),
                ('start_date', models.DateTimeField(verbose_name='დაწყების თარიღი')),
                ('end_date', models.DateTimeField(verbose_name='დასრულების თარიღი')),
            ],
            options={
                'verbose_name': 'ფასდაკლება',
                'verbose_name_plural': 'ფასდაკლებები',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='რაოდენობა')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ჯამური ფასი')),
                ('order_date', models.DateTimeField(verbose_name='შეკვეთის თარიღი')),
                ('status', models.IntegerField(choices=[(0, 'პროცესშია'), (1, 'მიღებულია')], default=0, max_length=255, verbose_name='სტატუსი')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='მომხმარებელი')),
            ],
            options={
                'verbose_name': 'შეკვეთა',
                'verbose_name_plural': 'შეკვეთები',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='სახელი')),
                ('description', ckeditor.fields.RichTextField(verbose_name='აღწერა')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ფასი')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='შექმნის თარიღი')),
                ('in_stock', models.PositiveIntegerField(default=0, verbose_name='მარაგში დარჩენილი რაოდენობა')),
                ('status', models.IntegerField(choices=[(0, 'ხელმისაწვდომი'), (1, 'მარაგში არ არის'), (2, 'Coming Soon'), (3, 'ფასდაკლება')], default=0, verbose_name='სტატუსი')),
                ('free_delivery', models.BooleanField(default=False, verbose_name='უფასო მიწოდება')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='სლაგი')),
                ('category', models.ManyToManyField(related_name='products', to='ecommerce.category', verbose_name='კატეგორია')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecommerce.discount', verbose_name='ფასდაკლება')),
            ],
            options={
                'verbose_name': 'პროდუქტი',
                'verbose_name_plural': 'პროდუქტები',
            },
        ),
        migrations.CreateModel(
            name='ProductSpecs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_name', models.CharField(max_length=255, verbose_name='სპეციფიკაციის სახელი')),
                ('spec_value', models.CharField(max_length=255, verbose_name='სპეციფიკაციის მნიშვნელობა')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_specs', to='ecommerce.product', verbose_name='პროდუქტი')),
            ],
            options={
                'verbose_name': 'სპეციფიკაცია',
                'verbose_name_plural': 'სპეციფიკაციები',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='ecommerce/product_images/', verbose_name='სურათი')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='ecommerce.product', verbose_name='პროდუქტი')),
            ],
            options={
                'verbose_name': 'პროდუქტის სურათი',
                'verbose_name_plural': 'პროდუქტის სურათები',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ManyToManyField(related_name='products', to='ecommerce.productimage', verbose_name='სურათი'),
        ),
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=models.ManyToManyField(related_name='products', to='ecommerce.productspecs', verbose_name='სპეციფიკაცია'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='თანხა')),
                ('payment_method', models.CharField(choices=[(0, 'ნაღდი ფული'), (1, 'ბარათით'), (2, 'სხვა')], default=1, max_length=255, verbose_name='გადახდის მეთოდი')),
                ('date', models.DateTimeField(verbose_name='თარიღი')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='ecommerce.order', verbose_name='შეკვეთა')),
            ],
            options={
                'verbose_name': 'გადახდა',
                'verbose_name_plural': 'გადახდები',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='ecommerce.product', verbose_name='პროდუქტი'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='რაოდენობა')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ჯამური ფასი')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to=settings.AUTH_USER_MODEL, verbose_name='მომხმარებელი')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='ecommerce.product', verbose_name='პროდუქტი')),
            ],
            options={
                'verbose_name': 'კალათა',
                'verbose_name_plural': 'კალათები',
            },
        ),
    ]
