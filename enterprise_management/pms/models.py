from django.utils.timezone import now
import uuid
from django.db import models

# Create your models here.
from pms.choices import CustomerType, MeansOfTransportation, OrderStatus, PaymentMethod, PaymentStatus, ShippingStatus


class Customer(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True, auto_created=True, editable=False)
    code = models.CharField(default=uuid.uuid4, editable=False, max_length=50, null=False)
    full_name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=15, null=False)
    type = models.CharField(max_length=50,choices=CustomerType.choices,default=CustomerType.INDIVIDUAL, null=False)
    shipping_address = models.TextField()
    billing_address = models.TextField()
    created_at = models.DateTimeField(editable=False, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, null=True, default=None)

    class Meta:
        # Specify the database table name
        db_table = 'customers'
        # Define default ordering by the 'created_at' field
        ordering = ['created_at']
        # Define a unique constraint for the 'code' field
        unique_together = [('code',)]
        # Set a human-readable name for the model
        verbose_name = 'Customer'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Customers'
        # Define permissions for the model
        permissions = [
            ('can_view_customer', 'Can view Customer'),
            ('can_change_customer', 'Can change Customer'),
        ]
    
    # The value we use for fields and relationships
    def __str__(self):
        return '%s' % (self.full_name)


class Collection(models.Model):
    id = models.IntegerField(primary_key=True, null=False,unique=True, auto_created=True, editable=False)
    name = models.CharField(editable=True, max_length=100, null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(editable=False, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, null=True, default=None)

    class Meta:
        # Specify the database table name
        db_table = 'collections'
        # Define default ordering by the 'created_at' field
        ordering = ['created_at']
        # Define a unique constraint for the 'code' field
        unique_together = [('id',)]
        # Set a human-readable name for the model
        verbose_name = 'Collection'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Collections'
        # Define permissions for the model
        permissions = [
            ('can_view_collection', 'Can view Collection'),
            ('can_change_collection', 'Can change Collection'),
        ] 
    
    def __str__(self):
        return '%s' % (self.name)


class Product(models.Model):
    id = models.IntegerField(primary_key=True, null=False,unique=True, auto_created=True, editable=False)
    name = models.CharField(editable=True, max_length=100, null=False)
    dimensions = models.CharField(editable=True, max_length=100, null=True)
    regular_price = models.FloatField(null=True)
    pro_price = models.FloatField(null=True)
    description = models.TextField(null=True)
    active = models.BooleanField(default=True)
    # check static path of this
    image = models.ImageField(upload_to="products/", blank=True)
    collection = models.ForeignKey('Collection', related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, null=True, default=None)

    class Meta:
        # Specify the database table name
        db_table = 'products'
        # Define default ordering by the 'created_at' field
        ordering = ['created_at']
        # Define a unique constraint for the 'code' field
        unique_together = [('id',)]
        # Set a human-readable name for the model
        verbose_name = 'Product'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Products'
        # Define permissions for the model
        permissions = [
            ('can_view_product', 'Can view Product'),
            ('can_change_product', 'Can change Product'),
        ] 
    
    def __str__(self):
        return '%s %s' % (self.name, self.collection.name)


class Order(models.Model):
    id = models.IntegerField(primary_key=True, null=False,unique=True, auto_created=True, editable=False)
    code = models.CharField(default=uuid.uuid4, editable=False, max_length=50, null=False)
    status = models.CharField(max_length=50,choices=OrderStatus.choices,default=OrderStatus.QUOTATION,)
    details = models.TextField()
    customer = models.ForeignKey("Customer", related_name='orders', on_delete=models.CASCADE)
    salesperson = models.ForeignKey("auth.User", related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, null=True, default=None)

    class Meta:
        # Specify the database table name
        db_table = 'orders'
        # Define default ordering by the 'order_created_at' field
        ordering = ['created_at']
        # Define a unique constraint for the 'order_code' field
        unique_together = [('code',)]
        # Set a human-readable name for the model
        verbose_name = 'Order'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Orders'
        # Define permissions for the model
        permissions = [
            ('can_view_order', 'Can view Order'),
            ('can_change_order', 'Can change Order'),
        ]

    def __str__(self):
        return '%s %s %s' % (self.status, self.code, self.customer.full_name)


class Cart(models.Model):
    id = models.IntegerField(primary_key=True, null=False,unique=True, auto_created=True, editable=False)
    code = models.CharField(default=uuid.uuid4, editable=False, max_length=50, null=False)
    quantity = models.IntegerField()
    order = models.ForeignKey('Order', related_name='carts', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', related_name='cart', on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, null=True, default=None)

    class Meta:
        # Specify the database table name
        db_table = 'carts'
        # Define default ordering by the 'cart_created_at' field
        ordering = ['created_at']
        # Define a unique constraint for the 'cart_code' field
        unique_together = [('code',)]
        # Set a human-readable name for the model
        verbose_name = 'Cart'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Carts'
        # Define permissions for the model
        permissions = [
            ('can_view_cart', 'Can view Cart'),
            ('can_change_cart', 'Can change Cart'),
        ] 
    
    def __str__(self):
        return '%s %s %s' % (self.code, self.order.code, self.product.name)


class Production(models.Model):
    id = models.IntegerField(primary_key=True, null=False,unique=True, auto_created=True, editable=False)
    code = models.CharField(default=uuid.uuid4, editable=False, max_length=50)
    task = models.TextField()
    order_date = models.DateTimeField(null=True, auto_now_add=True)
    delivery_date = models.DateField(default=None, null=True)
    cart = models.ForeignKey("Cart", related_name='production', on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, null=True, default=None)

    class Meta:
        # Specify the database table name
        db_table = 'productions'
        # Define default ordering by the 'order_created_at' field
        ordering = ['created_at']
        # Define a unique constraint for the 'order_code' field
        unique_together = [('code',)]
        # Set a human-readable name for the model
        verbose_name = 'Production'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Productions'
        # Define permissions for the model
        permissions = [
            ('can_view_production', 'Can view Production'),
            ('can_change_production', 'Can change Production'),
        ]
    
    # The value we use for fields and relationships
    def __str__(self):
        return '%s %s' % (self.task, f"delivered on {self.delivery_date}" if self.delivery_date else "not delivered")


class Billing(models.Model):
    id = models.IntegerField(primary_key=True, null=False,unique=True, auto_created=True, editable=False)
    code = models.CharField(default=uuid.uuid4, editable=False, max_length=50)
    total = models.FloatField()
    payment_method = models.CharField(max_length=50,choices=PaymentMethod.choices,default=PaymentMethod.CASH,)
    payment_status = models.CharField(max_length=50,choices=PaymentStatus.choices,default=PaymentStatus.DEPOSIT,)
    payment_date = models.DateTimeField(null=True, default=None)
    order = models.ForeignKey("Order", related_name='billings', on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, null=True, default=None)

    class Meta:
        # Specify the database table name
        db_table = 'billings'
        # Define default ordering by the 'order_created_at' field
        ordering = ['created_at']
        # Define a unique constraint for the 'order_code' field
        unique_together = [('code',)]
        # Set a human-readable name for the model
        verbose_name = 'Billing'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Billings'
        # Define permissions for the model
        permissions = [
            ('can_view_billing', 'Can view Billing'),
            ('can_change_billing', 'Can change Billing'),
        ]
    
    # The value we use for fields and relationships
    def __str__(self):
        return '%s %s' % (self.payment_status, self.order.customer.full_name)


class Shipping(models.Model):
    id = models.IntegerField(primary_key=True, null=False,unique=True, auto_created=True, editable=False)
    code = models.CharField(default=uuid.uuid4, editable=False, max_length=50)
    means_of_transportation = models.CharField(max_length=50,choices=MeansOfTransportation.choices,default=MeansOfTransportation.IN_STORE_PICKUP,)
    cost = models.FloatField()
    payment_type = models.CharField(max_length=50,choices=PaymentMethod.choices,default=PaymentMethod.CASH,)
    payment_date = models.DateTimeField(null=True, default=None)
    status = models.CharField(max_length=50,choices=ShippingStatus.choices,default=ShippingStatus.READY_TO_SHIP,)
    order = models.ForeignKey("Order", related_name="shipping", on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, null=True, default=None)

    class Meta:
        # Specify the database table name
        db_table = 'shippings'
        # Define default ordering by the 'order_created_at' field
        ordering = ['created_at']
        # Define a unique constraint for the 'order_code' field
        unique_together = [('code',)]
        # Set a human-readable name for the model
        verbose_name = 'Shipping'
        # Set the plural form of the model's verbose name
        verbose_name_plural = 'Shippings'
        # Define permissions for the model
        permissions = [
            ('can_view_shipping', 'Can view Shipping'),
            ('can_change_shipping', 'Can change Shipping'),
        ]
    
    # The value we use for fields and relationships
    def __str__(self):
        return '%s %s %s' % (self.status, self.means_of_transportation, self.order.customer.full_name)

