from django.contrib import admin

# Register your models here.

from .models import OilType, Brand, CarForSale, CarForRent,Car,UserProfile
admin.site.register(Car)
admin.site.register(UserProfile)
admin.site.register(OilType)
admin.site.register(Brand)
admin.site.register(CarForSale)
admin.site.register(CarForRent)
