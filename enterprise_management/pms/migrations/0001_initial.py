# Generated by Django 5.0.4 on 2024-04-15 12:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.IntegerField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('billing_order_total', models.FloatField()),
                ('billing_payment_method', models.CharField(choices=[('cash payment', 'Cash'), ('check payment', 'Check')], default='cash payment', max_length=50)),
                ('billing_payment_state', models.CharField(choices=[('deposit', 'Deposit'), ('payoff', 'Payoff')], default='deposit', max_length=50)),
                ('billing_payment_date', models.DateTimeField()),
                ('billing_created_at', models.DateTimeField(auto_now_add=True)),
                ('billing_updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Billing',
                'verbose_name_plural': 'Billings',
                'db_table': 'billings',
                'ordering': ['billing_created_at'],
                'permissions': [('can_view_billing', 'Can view Billing'), ('can_change_billing', 'Can change Billing')],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.IntegerField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('product_name', models.TextField()),
                ('product_code', models.TextField()),
                ('product_price', models.FloatField()),
                ('product_quantity', models.IntegerField()),
                ('cart_created_at', models.DateTimeField(auto_now_add=True)),
                ('cart_updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
                'db_table': 'carts',
                'ordering': ['cart_created_at'],
                'permissions': [('can_view_cart', 'Can view Cart'), ('can_change_cart', 'Can change Cart')],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('customer_full_name', models.CharField(max_length=100)),
                ('customer_email', models.CharField(max_length=50)),
                ('customer_phone_number', models.CharField(max_length=15)),
                ('customer_type', models.CharField(choices=[('reseller', 'Reseller'), ('individual', 'Individual')], default='individual', max_length=50)),
                ('customer_shipping_address', models.TextField()),
                ('customer_billing_address', models.TextField()),
                ('customer_created_at', models.DateTimeField(auto_now_add=True)),
                ('customer_updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'db_table': 'customers',
                'ordering': ['customer_created_at'],
                'permissions': [('can_view_customer', 'Can view Customer'), ('can_change_customer', 'Can change Customer')],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('order_state', models.CharField(choices=[('quotation', 'Quotation'), ('purchase order', 'Purchase Order'), ('proforma invoice', 'Proforma')], default='quotation', max_length=50)),
                ('order_details', models.TextField()),
                ('order_total', models.FloatField()),
                ('order_created_at', models.DateTimeField(auto_now_add=True)),
                ('order_updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'orders',
                'ordering': ['order_created_at'],
                'permissions': [('can_view_order', 'Can view Order'), ('can_change_order', 'Can change Order')],
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.IntegerField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('production_collection', models.TextField()),
                ('production_task', models.TextField()),
                ('production_order_date', models.DateTimeField()),
                ('production_delivery_date', models.DateField()),
                ('production_created_at', models.DateTimeField(auto_now_add=True)),
                ('production_updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Production',
                'verbose_name_plural': 'Productions',
                'db_table': 'productions',
                'ordering': ['production_created_at'],
                'permissions': [('can_view_production', 'Can view Production'), ('can_change_production', 'Can change Production')],
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.IntegerField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('shipping_means_of_transportation', models.CharField(choices=[('standard delivery', 'Standard Delivery'), ('express delivery', 'Express Delivery'), ('in-store pickup', 'In Store Pickup'), ('courier service', 'Courier Service'), ('freight transport', 'Freight Transport'), ('specialized transport', 'Specialized Transport')], default='in-store pickup', max_length=50)),
                ('shipping_cost', models.FloatField()),
                ('shipping_payment_type', models.CharField(choices=[('cash payment', 'Cash'), ('check payment', 'Check')], default='cash payment', max_length=50)),
                ('shipping_payment_date', models.DateField()),
                ('shipping_status', models.CharField(choices=[('cash payment', 'Cash'), ('check payment', 'Check')], default='cash payment', max_length=50)),
                ('shipping_created_at', models.DateTimeField(auto_now_add=True)),
                ('shipping_updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Shipping',
                'verbose_name_plural': 'Shippings',
                'db_table': 'shippings',
                'ordering': ['shipping_created_at'],
                'permissions': [('can_view_shipping', 'Can view Shipping'), ('can_change_shipping', 'Can change Shipping')],
            },
        ),
    ]
