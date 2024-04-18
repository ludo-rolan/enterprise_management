from django.contrib.auth.models import Group, User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view

from pms.serializers import BillingSerializer, CartSerializer, CollectionSerializer, CustomerSerializer, GroupSerializer, MyTokenObtainPairSerializer, OrderSerializer, ProductSerializer, ProductionSerializer, ShippingSerializer, UserSerializer
from pms.models import Billing, Cart, Collection, Customer, Order, Product, Production, Shipping

from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('created_at')
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

class CollectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows collections to be viewed or edited.
    """
    queryset = Collection.objects.all().order_by('created_at')
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('created_at')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all().order_by('created_at')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows carts to be viewed or edited.
    """
    queryset = Cart.objects.all().order_by('created_at')
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows productions to be viewed or edited.
    """
    queryset = Production.objects.all().order_by('created_at')
    serializer_class = ProductionSerializer
    permission_classes = [permissions.IsAuthenticated]


class BillingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows billings to be viewed or edited.
    """
    queryset = Billing.objects.all().order_by('created_at')
    serializer_class = BillingSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShippingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shippings to be viewed or edited.
    """
    queryset = Shipping.objects.all().order_by('created_at')
    serializer_class = ShippingSerializer
    permission_classes = [permissions.IsAuthenticated]


# @api_view(['GET', 'POST'])
# def customer_list(request):
#     """
#     List all customers, or create a new customer.
#     """
#     if request.method == 'GET':
#         customers = Customer.objects.all()
#         serializer = CustomerSerializer(customers, many=True)
#         return JsonResponse(serializer.data)

#     elif request.method == 'POST':
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def customer_detail(request, pk):
#     """
#     Retrieve, update or delete a customer.
#     """
#     try:
#         customer = Customer.objects.get(pk=pk)
#     except Customer.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CustomerSerializer(customer)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CustomerSerializer(customer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         customer.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def order_list(request):
#     """
#     List all orders, or create a new order.
#     """
#     if request.method == 'GET':
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return JsonResponse(serializer.data)

#     elif request.method == 'POST':
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def order_detail(request, pk):
#     """
#     Retrieve, update or delete an order.
#     """
#     try:
#         order = Order.objects.get(pk=pk)
#     except Customer.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = OrderSerializer(order)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         serializer = OrderSerializer(order, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         order.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def cart_list(request):
#     """
#     List all carts, or create a new cart.
#     """
#     if request.method == 'GET':
#         carts = Cart.objects.all()
#         serializer = CartSerializer(carts, many=True)
#         return JsonResponse(serializer.data)

#     elif request.method == 'POST':
#         serializer = CartSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def cart_detail(request, pk):
#     """
#     Retrieve, update or delete a cart.
#     """
#     try:
#         cart = Cart.objects.get(pk=pk)
#     except Cart.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CartSerializer(cart)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CartSerializer(cart, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         cart.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def production_list(request):
#     """
#     List all carts, or create a new cart.
#     """
#     if request.method == 'GET':
#         productions = Production.objects.all()
#         serializer = ProductionSerializer(productions, many=True)
#         return JsonResponse(serializer.data)

#     elif request.method == 'POST':
#         serializer = ProductionSerializer(data=request.data, safe=False)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def production_detail(request, pk):
#     """
#     Retrieve, update or delete a cart.
#     """
#     try:
#         production = Production.objects.get(pk=pk)
#     except Cart.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProductionSerializer(production)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ProductionSerializer(production, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         production.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def billing_list(request):
#     """
#     List all bills, or create a new bill.
#     """
#     if request.method == 'GET':
#         billings = Billing.objects.all()
#         serializer = BillingSerializer(billings, many=True)
#         return JsonResponse(serializer.data)

#     elif request.method == 'POST':
#         serializer = BillingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def billing_detail(request, pk):
#     """
#     Retrieve, update or delete a bill.
#     """
#     try:
#         billing = Billing.objects.get(pk=pk)
#     except Cart.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = BillingSerializer(billing)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         serializer = BillingSerializer(billing, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         billing.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def shipping_list(request):
#     """
#     List all shippings, or create a new shipping.
#     """
#     if request.method == 'GET':
#         shippings = Shipping.objects.all()
#         serializer = BillingSerializer(shippings, many=True)
#         return JsonResponse(serializer.data)

#     elif request.method == 'POST':
#         serializer = ShippingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def shipping_detail(request, pk):
#     """
#     Retrieve, update or delete a shipping.
#     """
#     try:
#         shipping = Shipping.objects.get(pk=pk)
#     except Shipping.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ShippingSerializer(shipping)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ShippingSerializer(shipping, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         shipping.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
