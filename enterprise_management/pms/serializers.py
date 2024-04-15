from django.contrib.auth.models import Group, User
from rest_framework import serializers

from pms.choices import CustomerType, MeansOfTransportation, OrderState, PaymentMethod, PaymentState, ShippingStatus
from pms.models import Billing, Cart, Customer, Order, Production, Shipping


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# class CustomerSerializer(serializers.Serializer):
#     customer_code = serializers.CharField(read_only=True)
#     customer_full_name = serializers.CharField(required=True, allow_blank=False, max_length=50)
#     customer_email = serializers.CharField(required=True, allow_blank=False, max_length=50)
#     customer_phone_number = serializers.CharField(required=True, allow_blank=False, max_length=15)
#     customer_type = serializers.ChoiceField(choices=CustomerType.choices,default=CustomerType.INDIVIDUAL)
#     customer_shipping_address = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     customer_billing_address = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     customer_created_at = serializers.DateTimeField()
#     customer_updated_at = serializers.DateTimeField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Customer` instance, given the validated data.
#         """
#         return Customer.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Customer` instance, given the validated data.
#         """
#         instance.customer_code = validated_data.get('customer_code', instance.customer_code)
#         instance.customer_full_name = validated_data.get('customer_full_name', instance.customer_full_name)
#         instance.customer_email = validated_data.get('customer_email', instance.customer_full_name)
#         instance.customer_phone_number = validated_data.get('customer_phone_number', instance.customer_full_name)
#         instance.customer_type = validated_data.get('customer_type', instance.customer_full_name)
#         instance.customer_shipping_address = validated_data.get('customer_shipping_address', instance.customer_full_name)
#         instance.customer_billing_address = validated_data.get('customer_billing_address', instance.customer_full_name)
#         instance.customer_created_at = validated_data.get('customer_created_at', instance.customer_created_at)
#         instance.customer_updated_at = validated_data.get('customer_updated_at', instance.customer_updated_at)
        
#         instance.save()
#         return instance


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'customer_code', 
            'customer_full_name', 
            'customer_email', 
            'customer_phone_number',
            'customer_type',
            'customer_shipping_address',
            'customer_billing_address',
            'customer_created_at',
            'customer_updated_at'
        ]


# class OrderSerializer(serializers.Serializer):
#     order_code = serializers.CharField(read_only=True)
#     order_state = serializers.ChoiceField(choices=OrderState.choices,default=OrderState.QUOTATION)
#     order_details = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     order_total = serializers.FloatField(required=True, allow_blank=False)
#     order_created_at = serializers.DateTimeField()
#     order_updated_at = serializers.DateTimeField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Customer` instance, given the validated data.
#         """
#         return Order.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Customer` instance, given the validated data.
#         """
#         instance.order_code = validated_data.get('order_code', instance.order_code)
#         instance.order_state = validated_data.get('order_state', instance.order_state)
#         instance.order_details = validated_data.get('order_details', instance.order_details)
#         instance.order_total = validated_data.get('order_total', instance.order_total)
#         instance.order_created_at = validated_data.get('order_created_at', instance.order_created_at)
#         instance.order_updated_at = validated_data.get('order_updated_at', instance.order_updated_at)
        
#         instance.save()
#         return instance


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'order_code', 
            'order_state', 
            'order_details', 
            'order_total',
            'order_created_at',
            'order_updated_at',
        ]


# class CartSerializer(serializers.Serializer):
#     cart_code = serializers.CharField(read_only=True)
#     product_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     product_code = serializers.CharField(required=True, allow_blank=False, max_length=50)
#     product_price = serializers.FloatField(required=True, allow_blank=False)
#     product_quantity = serializers.IntegerField(required=True, allow_blank=False)
#     cart_created_at = serializers.DateTimeField()
#     cart_updated_at = serializers.DateTimeField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Customer` instance, given the validated data.
#         """
#         return Cart.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Customer` instance, given the validated data.
#         """
#         instance.cart_code = validated_data.get('cart_code', instance.cart_code)
#         instance.product_name = validated_data.get('product_name', instance.product_name)
#         instance.product_code = validated_data.get('product_code', instance.product_code)
#         instance.product_price = validated_data.get('product_price', instance.product_price)
#         instance.product_quantity = validated_data.get('product_quantity', instance.product_quantity)
#         instance.product_created_at = validated_data.get('product_created_at', instance.product_created_at)
#         instance.product_updated_at = validated_data.get('product_updated_at', instance.product_updated_at)
        
#         instance.save()
#         return instance


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'id',
            'cart_code', 
            'product_name', 
            'product_code', 
            'product_price',
            'product_quantity',
            'product_created_at',
            'product_updated_at',
        ]


# class ProductionSerializer(serializers.Serializer):
#     production_code = serializers.CharField(read_only=True)
#     production_collection = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     production_task = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     production_order_date = serializers.DateField()
#     production_delivery_date = serializers.DateField()
#     production_created_at = serializers.DateTimeField()
#     production_updated_at = serializers.DateTimeField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Customer` instance, given the validated data.
#         """
#         return Customer.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Customer` instance, given the validated data.
#         """
#         instance.production_code = validated_data.get('production_code', instance.production_code)
#         instance.production_collection = validated_data.get('production_collection', instance.production_collection)
#         instance.production_task = validated_data.get('production_task', instance.production_task)
#         instance.production_order_date = validated_data.get('production_order_date', instance.production_order_date)
#         instance.production_delivery_date = validated_data.get('production_delivery_date', instance.production_delivery_date)
#         instance.production_created_at = validated_data.get('production_created_at', instance.production_created_at)
#         instance.production_updated_at = validated_data.get('production_updated_at', instance.production_updated_at)
        
#         instance.save()
#         return instance


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = [
            'id',
            'production_code', 
            'production_collection', 
            'production_task', 
            'production_order_date',
            'production_delivery_date',
            'production_created_at',
            'production_updated_at',
        ]


# class BillingSerializer(serializers.Serializer):
#     billing_code = serializers.CharField(read_only=True)
#     billing_order_total = serializers.FloatField(required=True, allow_blank=False)
#     billing_payment_method = serializers.CharField(required=True, allow_blank=False, choices=PaymentMethod.choices, default=PaymentMethod.CASH, max_length=50)
#     billing_payment_state = serializers.CharField(required=True, allow_blank=False, choices=PaymentState.choices, default=PaymentState.DEPOSIT, max_length=50)
#     billing_payment_date = serializers.DateTimeField()
#     billing_created_at = serializers.DateTimeField()
#     billing_updated_at = serializers.DateTimeField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Customer` instance, given the validated data.
#         """
#         return Customer.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Customer` instance, given the validated data.
#         """
#         instance.billing_code = validated_data.get('billing_code', instance.billing_code)
#         instance.billing_order_total = validated_data.get('billing_order_total', instance.billing_order_total)
#         instance.billing_payment_method = validated_data.get('billing_payment_method', instance.billing_payment_method)
#         instance.billing_payment_state = validated_data.get('billing_payment_state', instance.billing_payment_state)
#         instance.billing_payment_date = validated_data.get('billing_payment_date', instance.billing_payment_date)
#         instance.billing_created_at = validated_data.get('billing_created_at', instance.billing_created_at)
#         instance.billing_updated_at = validated_data.get('billing_updated_at', instance.billing_updated_at)
        
#         instance.save()
#         return instance


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = [
            'id',
            'billing_code', 
            'billing_order_total', 
            'billing_payment_method', 
            'billing_payment_state',
            'billing_payment_date',
            'billing_created_at',
            'billing_updated_at',
        ]


# class ShippingSerializer(serializers.Serializer):
#     shipping_code = serializers.CharField(read_only=True)
#     shipping_means_of_transportation = serializers.CharField(required=True, allow_blank=False, choices=MeansOfTransportation.choices,default=MeansOfTransportation.IN_STORE_PICKUP)
#     shipping_cost = serializers.FloatField(required=True, allow_blank=False)
#     shipping_payment_type = serializers.CharField(required=True, allow_blank=False, choices=PaymentMethod.choices,default=PaymentMethod.CASH)
#     shipping_payment_date = serializers.DateField()
#     shipping_status = serializers.CharField(required=True, allow_blank=False, choices=ShippingStatus.choices,default=ShippingStatus.READY_TO_SHIP)
#     shipping_created_at = serializers.DateTimeField()
#     shipping_updated_at = serializers.DateTimeField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Customer` instance, given the validated data.
#         """
#         return Customer.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Customer` instance, given the validated data.
#         """
#         instance.shipping_code = validated_data.get('shipping_code', instance.shipping_code)
#         instance.shipping_means_of_transportation = validated_data.get('shipping_means_of_transportation', instance.shipping_means_of_transportation)
#         instance.shipping_cost = validated_data.get('shipping_cost', instance.shipping_cost)
#         instance.shipping_payment_type = validated_data.get('shipping_payment_type', instance.shipping_payment_type)
#         instance.shipping_payment_date = validated_data.get('shipping_payment_date', instance.shipping_payment_date)
#         instance.shipping_status = validated_data.get('shipping_status', instance.shipping_status)
#         instance.shipping_created_at = validated_data.get('shipping_created_at', instance.shipping_created_at)
#         instance.shipping_updated_at = validated_data.get('shipping_updated_at', instance.shipping_updated_at)
        
#         instance.save()
#         return instance
    

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = [
            'id',
            'shipping_code', 
            'shipping_means_of_transportation', 
            'shipping_cost', 
            'shipping_payment_type',
            'shipping_payment_date',
            'shipping_status',
            'shipping_created_at',
            'shipping_updated_at',
        ]
