from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')
    search_fields=('name',)
    list_filter=('price','stock')
admin.site.register(Product,ProductAdmin)


admin.site.register(CustomUser)

class OrderAdmin(admin.ModelAdmin):
    list_display=('user','created_at','total_price')
    search_fields=('user__username','id')
    list_filter=('created_at',)
  
admin.site.register(Order,OrderAdmin)

