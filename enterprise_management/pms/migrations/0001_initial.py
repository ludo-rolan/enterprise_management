# Generated by Django 5.0.4 on 2024-04-22 14:09

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(default=None, editable=False, null=True)),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
                'db_table': 'collections',
                'ordering': ['created_at'],
                'permissions': [('can_view_collection', 'Can view Collection'), ('can_change_collection', 'Can change Collection')],
                'unique_together': {('id',)},
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(default=uuid.uuid4, editable=False, max_length=50)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('type', models.CharField(choices=[('reseller', 'Reseller'), ('individual', 'Individual')], default='individual', max_length=50)),
                ('shipping_address', models.TextField()),
                ('billing_address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(default=None, editable=False, null=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'db_table': 'customers',
                'ordering': ['created_at'],
                'permissions': [('can_view_customer', 'Can view Customer'), ('can_change_customer', 'Can change Customer')],
                'unique_together': {('code',)},
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(default=uuid.uuid4, editable=False, max_length=50)),
                ('status', models.CharField(choices=[('quotation', 'Quotation'), ('purchase order', 'Purchase Order'), ('proforma invoice', 'Proforma')], default='quotation', max_length=50)),
                ('details', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(default=None, editable=False, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='pms.customer')),
                ('salesperson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'orders',
                'ordering': ['created_at'],
                'permissions': [('can_view_order', 'Can view Order'), ('can_change_order', 'Can change Order')],
                'unique_together': {('code',)},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('dimensions', models.CharField(max_length=100, null=True)),
                ('regular_price', models.FloatField(null=True)),
                ('pro_price', models.FloatField(null=True)),
                ('description', models.TextField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, upload_to='products/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(default=None, editable=False, null=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='pms.collection')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
                'ordering': ['created_at'],
                'permissions': [('can_view_product', 'Can view Product'), ('can_change_product', 'Can change Product')],
                'unique_together': {('id',)},
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(default=uuid.uuid4, editable=False, max_length=50)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(default=None, editable=False, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='pms.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='pms.product')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
                'db_table': 'carts',
                'ordering': ['created_at'],
                'permissions': [('can_view_cart', 'Can view Cart'), ('can_change_cart', 'Can change Cart')],
                'unique_together': {('code',)},
            },
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(default=uuid.uuid4, editable=False, max_length=50)),
                ('total', models.FloatField()),
                ('payment_method', models.CharField(choices=[('cash payment', 'Cash'), ('check payment', 'Check')], default='cash payment', max_length=50)),
                ('payment_status', models.CharField(choices=[('deposit', 'Deposit'), ('payoff', 'Payoff')], default='deposit', max_length=50)),
                ('payment_date', models.DateTimeField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(default=None, editable=False, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billings', to='pms.order')),
            ],
            options={
                'verbose_name': 'Billing',
                'verbose_name_plural': 'Billings',
                'db_table': 'billings',
                'ordering': ['created_at'],
                'permissions': [('can_view_billing', 'Can view Billing'), ('can_change_billing', 'Can change Billing')],
                'unique_together': {('code',)},
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(default=uuid.uuid4, editable=False, max_length=50)),
                ('task', models.TextField()),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('delivery_date', models.DateField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(default=None, editable=False, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production', to='pms.cart')),
            ],
            options={
                'verbose_name': 'Production',
                'verbose_name_plural': 'Productions',
                'db_table': 'productions',
                'ordering': ['created_at'],
                'permissions': [('can_view_production', 'Can view Production'), ('can_change_production', 'Can change Production')],
                'unique_together': {('code',)},
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(default=uuid.uuid4, editable=False, max_length=50)),
                ('means_of_transportation', models.CharField(choices=[('standard delivery', 'Standard Delivery'), ('express delivery', 'Express Delivery'), ('in-store pickup', 'In Store Pickup'), ('courier service', 'Courier Service'), ('freight transport', 'Freight Transport'), ('specialized transport', 'Specialized Transport')], default='in-store pickup', max_length=50)),
                ('cost', models.FloatField()),
                ('payment_type', models.CharField(choices=[('cash payment', 'Cash'), ('check payment', 'Check')], default='cash payment', max_length=50)),
                ('payment_date', models.DateTimeField(default=None, null=True)),
                ('status', models.CharField(choices=[('ready to ship', 'Ready To Ship'), ('in transit', 'In Transit'), ('order completed', 'Order Completed')], default='ready to ship', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(default=None, editable=False, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping', to='pms.order')),
            ],
            options={
                'verbose_name': 'Shipping',
                'verbose_name_plural': 'Shippings',
                'db_table': 'shippings',
                'ordering': ['created_at'],
                'permissions': [('can_view_shipping', 'Can view Shipping'), ('can_change_shipping', 'Can change Shipping')],
                'unique_together': {('code',)},
            },
        ),
    ]
