from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Billing)
admin.site.register(Products)
admin.site.register(Amount)