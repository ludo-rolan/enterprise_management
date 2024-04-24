from django.contrib.auth.models import Group, User
from rest_framework import serializers

from pms.models import Collection, Customer, Billing, Product, Production, Shipping, Order, Cart
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'code', 
            'full_name', 
            'email', 
            'phone_number',
            'type',
            'shipping_address',
            'billing_address',
            'created_at',
            'updated_at'
        ]


class CollectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Collection
        fields = [
            'id',
            'name',
            'description',
            'created_at',
            'updated_at'
        ]


class ProductSerializer(serializers.ModelSerializer):
    collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'dimensions',
            'regular_price',
            'pro_price',
            'description',
            'active',
            'image',
            'collection',
            'created_at',
            'updated_at'
        ]


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    salesperson = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = Order
        fields = [
            'id',
            'code', 
            'status', 
            'details', 
            'customer',
            'salesperson',
            'created_at',
            'updated_at',
        ]


class CartSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = Cart
        fields = [
            'id',
            'code',
            'quantity',
            'order',
            'product',
            'created_at',
            'updated_at',
        ]


class ProductionSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())
    
    class Meta:
        model = Production
        fields = [
            'id',
            'code',
            'task',
            'order_date',
            'delivery_date',
            'cart', 
            'created_at',
            'updated_at',
        ]


class BillingSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    
    class Meta:
        model = Billing
        fields = [
            'id',
            'code',
            'total', 
            'payment_method', 
            'payment_status',
            'payment_date',
            'order',
            'created_at',
            'updated_at',
        ]


class ShippingSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    
    class Meta:
        model = Shipping
        fields = [
            'id',
            'code', 
            'means_of_transportation', 
            'cost', 
            'payment_type',
            'payment_date',
            'status',
            'order',
            'created_at',
            'updated_at',
        ]
