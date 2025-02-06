from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.User)
admin.site.register(models.Discount)
admin.site.register(models.Collection)
admin.site.register(models.Order)
admin.site.register(models.OrderItems)
admin.site.register(models.OrderDiscount)
admin.site.register(models.Review)
admin.site.register(models.Wishlist)

