from django.contrib.auth.models import Group, User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, viewsets

from pms.serializers import BillingSerializer, CartSerializer, CustomerSerializer, GroupSerializer, OrderSerializer, ProductionSerializer, ShippingSerializer, UserSerializer
from pms.models import Billing, Cart, Customer, Order, Production, Shipping

from rest_framework.parsers import JSONParser


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


@csrf_exempt
def customer_list(request):
    """
    List all customers, or create a new customer.
    """
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def customer_detail(request, pk):
    """
    Retrieve, update or delete a customer.
    """
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(customer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=204)


@csrf_exempt
def order_list(request):
    """
    List all orders, or create a new order.
    """
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def order_detail(request, pk):
    """
    Retrieve, update or delete an order.
    """
    try:
        order = Order.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        order.delete()
        return HttpResponse(status=204)



@csrf_exempt
def cart_list(request):
    """
    List all carts, or create a new cart.
    """
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def cart_detail(request, pk):
    """
    Retrieve, update or delete a cart.
    """
    try:
        cart = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CartSerializer(cart)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CartSerializer(cart, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cart.delete()
        return HttpResponse(status=204)


@csrf_exempt
def production_list(request):
    """
    List all carts, or create a new cart.
    """
    if request.method == 'GET':
        productions = Production.objects.all()
        serializer = ProductionSerializer(productions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def production_detail(request, pk):
    """
    Retrieve, update or delete a cart.
    """
    try:
        production = Production.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductionSerializer(production)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductionSerializer(production, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        production.delete()
        return HttpResponse(status=204)


@csrf_exempt
def billing_list(request):
    """
    List all bills, or create a new bill.
    """
    if request.method == 'GET':
        billings = Billing.objects.all()
        serializer = BillingSerializer(billings, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BillingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def billing_detail(request, pk):
    """
    Retrieve, update or delete a bill.
    """
    try:
        billing = Billing.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BillingSerializer(billing)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BillingSerializer(billing, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        billing.delete()
        return HttpResponse(status=204)


@csrf_exempt
def billing_list(request):
    """
    List all bills, or create a new bill.
    """
    if request.method == 'GET':
        billings = Billing.objects.all()
        serializer = BillingSerializer(billings, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BillingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def billing_detail(request, pk):
    """
    Retrieve, update or delete a bill.
    """
    try:
        billing = Billing.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BillingSerializer(billing)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BillingSerializer(billing, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        billing.delete()
        return HttpResponse(status=204)


@csrf_exempt
def shipping_list(request):
    """
    List all shippings, or create a new shipping.
    """
    if request.method == 'GET':
        shippings = Shipping.objects.all()
        serializer = BillingSerializer(shippings, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShippingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def shipping_detail(request, pk):
    """
    Retrieve, update or delete a shipping.
    """
    try:
        shipping = Shipping.objects.get(pk=pk)
    except Shipping.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ShippingSerializer(shipping)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShippingSerializer(shipping, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        shipping.delete()
        return HttpResponse(status=204)


