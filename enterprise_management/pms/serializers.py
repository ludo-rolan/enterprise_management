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


# this is to customize the field to obtain a better value
class SalespersonField(serializers.RelatedField):
    def to_representation(self, value):
        customer = User.objects.filter(id=value.id).values('username')[0]
        return '%s' % (customer['username'])


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

# this is to customize the field to obtain a better value
class CustomerField(serializers.RelatedField):
    def to_representation(self, value):
        customer = Customer.objects.filter(id=value.id).values('full_name')[0]
        return '%s' % (customer['full_name'])


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


# this is to customize the field to obtain a better value
class CollectionField(serializers.RelatedField):
    def to_representation(self, value):
        collection = Collection.objects.filter(id=value.id).values('name')[0]
        return '%s' % (collection['name'])


class ProductSerializer(serializers.ModelSerializer):
    CollectionField(queryset=Collection.objects.all(), many=False)
    
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


# this is to customize the field to obtain a better value
class ProductField(serializers.RelatedField):
    def to_representation(self, value):
        product = Product.objects.filter(id=value.id).values('name')[0]
        return '%s' % (product['name'])


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerField(queryset=Customer.objects.all(), many=False)
    salesperson = SalespersonField(queryset=User.objects.all(), many=False)
    
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


# this is to customize the field to obtain a better value
class OrderField(serializers.RelatedField):
    def to_representation(self, value):
        order = Order.objects.filter(id=value.id).values('customer_id')[0]
        customer = Customer.objects.filter(id=order['customer_id']).values('full_name')[0]
        return '%s' % (customer['full_name'])


class CartSerializer(serializers.ModelSerializer):
    order = OrderField(queryset=Order.objects.all(), many=False)
    product = ProductField(queryset=Order.objects.all(), many=False)
    
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


# this is to customize the field to obtain a better value
class CartField(serializers.RelatedField):
    def to_representation(self, value):
        cart = Cart.objects.filter(id=value.id).values('code')[0]
        return '%s' % (cart['code'])


class ProductionSerializer(serializers.ModelSerializer):
    cart = CartField(queryset=Cart.objects.all(), many=False)
    
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
    order = OrderField(queryset=Order.objects.all(), many=False)
    
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
    order = OrderField(queryset=Order.objects.all(), many=False)
    
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
