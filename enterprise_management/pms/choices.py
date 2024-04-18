from django.db import models


class CustomerType(models.TextChoices):
    RESELLER = 'reseller'
    INDIVIDUAL = 'individual'

class OrderStatus(models.TextChoices):
    QUOTATION = 'quotation'
    PURCHASE_ORDER = 'purchase order'
    PROFORMA = 'proforma invoice'

class PaymentMethod(models.TextChoices):
    CASH = 'cash payment'
    CHECK = 'check payment'

class PaymentStatus(models.TextChoices):
    DEPOSIT = 'deposit'
    PAYOFF = 'payoff'

class MeansOfTransportation(models.TextChoices):
    STANDARD_DELIVERY = 'standard delivery'
    EXPRESS_DELIVERY = 'express delivery'
    IN_STORE_PICKUP = 'in-store pickup'
    COURIER_SERVICE = 'courier service'
    FREIGHT_TRANSPORT = 'freight transport'
    SPECIALIZED_TRANSPORT = 'specialized transport'

class ShippingStatus(models.TextChoices):
    READY_TO_SHIP = 'ready to ship'
    IN_TRANSIT = 'in transit'
    ORDER_COMPLETED = 'order completed'
