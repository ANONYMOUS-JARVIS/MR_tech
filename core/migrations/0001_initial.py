# Generated by Django 5.0.7 on 2024-08-06 15:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


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
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order_items_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_item_checkbox', models.BooleanField(default=False)),
                ('order_quantity', models.IntegerField(default=1)),
                ('order_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders_list_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_list_start_time', models.DateTimeField(auto_now_add=True)),
                ('order_list_ordered_checkbox', models.BooleanField(default=False)),
                ('order_list_order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('date_of_payment', models.DateTimeField(auto_now_add=True)),
                ('order_delivered', models.BooleanField(default=False)),
                ('order_received', models.BooleanField(default=False)),
                ('order_list_items', models.ManyToManyField(to='core.order_items_models')),
                ('order_list_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=32)),
                ('price', models.IntegerField(null=True)),
                ('description', models.TextField()),
                ('product_quantity', models.IntegerField(default=1)),
                ('product_image', models.ImageField(null=True, upload_to='image/')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
        migrations.AddField(
            model_name='order_items_models',
            name='order_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
    ]
