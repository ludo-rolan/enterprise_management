import enum
import uuid
from django.db import models

# Create your models here.
from django.db import models

from pms.choices import CustomerType, MeansOfTransportation, OrderState, PaymentMethod, PaymentState


class Customer(models.Model):
    
    # class CustomerType(models.TextChoices):
    #     RESELLER = 'reseller'
    #     INDIVIDUAL = 'individual'
    
    id = models.IntegerField(primary_key=True, null=False, unique=True, auto_created=True)
    customer_code = models.CharField(default=uuid.uuid4, editable=False, max_length=50, null=False)
    customer_full_name = models.CharField(max_length=100, null=False)
    customer_email = models.CharField(max_length=50, null=False)
    customer_phone_number = models.CharField(max_length=15, null=False)
    customer_type = models.CharField(max_length=50,choices=CustomerType.choices,default=CustomerType.INDIVIDUAL, null=False)
    customer_shipping_address = models.TextField()
    customer_billing_address = models.TextField()
    customer_created_at = models.DateTimeField(auto_now_add=True)
    customer_updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Specify the database table name
        db_table = 'customers'
        # Define default ordering by the 'customer_created_at' field
        ordering = ['customer_created_at']
        # Define a unique constraint for the 'customer_code' field
        unique_together = [('customer_code',)]
        # Set a human-readable name for the model
        verbose_name = 'Customer'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Customers'
        # Define permissions for the model
        permissions = [
            ('can_view_customer', 'Can view Customer'),
            ('can_change_customer', 'Can change Customer'),
        ]


class Order(models.Model):
    id = models.IntegerField(primary_key=True, null=False,unique=True, auto_created=True)
    order_code = models.CharField(default=uuid.uuid4, editable=False, max_length=50, null=False)
    order_state = models.CharField(max_length=50,choices=OrderState.choices,default=OrderState.QUOTATION,)
    order_details = models.TextField()
    order_total = models.FloatField()
    order_created_at = models.DateTimeField(auto_now_add=True)
    order_updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Specify the database table name
        db_table = 'orders'
        # Define default ordering by the 'order_created_at' field
        ordering = ['order_created_at']
        # Define a unique constraint for the 'order_code' field
        unique_together = [('order_code',)]
        # Set a human-readable name for the model
        verbose_name = 'Order'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Orders'
        # Define permissions for the model
        permissions = [
            ('can_view_order', 'Can view Order'),
            ('can_change_order', 'Can change Order'),
        ]


class Cart(models.Model):
    id = models.IntegerField(primary_key=True, null=False,unique=True, auto_created=True)
    cart_code = models.CharField(default=uuid.uuid4, editable=False, max_length=50, null=False)
    product_name = models.TextField()
    product_code = models.TextField()
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    cart_created_at = models.DateTimeField(auto_now_add=True)
    cart_updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Specify the database table name
        db_table = 'carts'
        # Define default ordering by the 'order_created_at' field
        ordering = ['cart_created_at']
        # Define a unique constraint for the 'order_code' field
        unique_together = [('cart_code',)]
        # Set a human-readable name for the model
        verbose_name = 'Cart'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Carts'
        # Define permissions for the model
        permissions = [
            ('can_view_cart', 'Can view Cart'),
            ('can_change_cart', 'Can change Cart'),
        ]


class Production(models.Model):
    id = models.IntegerField(primary_key=True, null=False,unique=True, auto_created=True)
    production_code = models.CharField(default=uuid.uuid4, editable=False, max_length=50)
    production_collection = models.TextField()
    production_task = models.TextField()
    production_order_date = models.DateTimeField()
    production_delivery_date = models.DateField()
    production_created_at = models.DateTimeField(auto_now_add=True)
    production_updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Specify the database table name
        db_table = 'productions'
        # Define default ordering by the 'order_created_at' field
        ordering = ['production_created_at']
        # Define a unique constraint for the 'order_code' field
        unique_together = [('production_code',)]
        # Set a human-readable name for the model
        verbose_name = 'Production'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Productions'
        # Define permissions for the model
        permissions = [
            ('can_view_production', 'Can view Production'),
            ('can_change_production', 'Can change Production'),
        ]


class Billing(models.Model):
    id = models.IntegerField(primary_key=True, null=False,unique=True, auto_created=True)
    billing_code = models.CharField(default=uuid.uuid4, editable=False, max_length=50)
    billing_order_total = models.FloatField()
    billing_payment_method = models.CharField(max_length=50,choices=PaymentMethod.choices,default=PaymentMethod.CASH,)
    billing_payment_state = models.CharField(max_length=50,choices=PaymentState.choices,default=PaymentState.DEPOSIT,)
    billing_payment_date = models.DateTimeField()
    billing_created_at = models.DateTimeField(auto_now_add=True)
    billing_updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Specify the database table name
        db_table = 'billings'
        # Define default ordering by the 'order_created_at' field
        ordering = ['billing_created_at']
        # Define a unique constraint for the 'order_code' field
        unique_together = [('billing_code',)]
        # Set a human-readable name for the model
        verbose_name = 'Billing'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Billings'
        # Define permissions for the model
        permissions = [
            ('can_view_billing', 'Can view Billing'),
            ('can_change_billing', 'Can change Billing'),
        ]


class Shipping(models.Model):
    id = models.IntegerField(primary_key=True, null=False,unique=True, auto_created=True)
    shipping_code = models.CharField(default=uuid.uuid4, editable=False, max_length=50)
    shipping_means_of_transportation = models.CharField(max_length=50,choices=MeansOfTransportation.choices,default=MeansOfTransportation.IN_STORE_PICKUP,)
    shipping_cost = models.FloatField()
    shipping_payment_type = models.CharField(max_length=50,choices=PaymentMethod.choices,default=PaymentMethod.CASH,)
    shipping_payment_date = models.DateField()
    shipping_status = models.CharField(max_length=50,choices=PaymentMethod.choices,default=PaymentMethod.CASH,)
    shipping_created_at = models.DateTimeField(auto_now_add=True)
    shipping_updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Specify the database table name
        db_table = 'shippings'
        # Define default ordering by the 'order_created_at' field
        ordering = ['shipping_created_at']
        # Define a unique constraint for the 'order_code' field
        unique_together = [('shipping_code',)]
        # Set a human-readable name for the model
        verbose_name = 'Shipping'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Shippings'
        # Define permissions for the model
        permissions = [
            ('can_view_shipping', 'Can view Shipping'),
            ('can_change_shipping', 'Can change Shipping'),
        ]