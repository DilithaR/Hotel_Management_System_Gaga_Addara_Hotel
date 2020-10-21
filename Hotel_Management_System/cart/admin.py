from django.contrib import admin
from cart.models import shopCart

# Register your models here.

class shopCartAdmin(admin.ModelAdmin):
    list_display = ['item','user','quantity','price','amount']
    list_filter = ['user']

admin.site.register(shopCart,shopCartAdmin)
