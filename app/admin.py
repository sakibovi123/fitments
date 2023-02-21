from django.contrib import admin
from .models import *


admin.site.register([
        Category,
        SubCategory,
        Brand,
        MultiImage,
        Product,
        Cart,
        Order,
        PaymentMethod,
        DeliveryMethod
    ])
