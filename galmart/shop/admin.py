from django.contrib import admin
from .models import Shop, Order, RecordedOrder


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name','open']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','shop','amount','status']

class RecordedOrderAdmin(admin.ModelAdmin):
    list_display = ['id','order_id','order_amount','shop']

admin.site.register(Shop,ShopAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(RecordedOrder,RecordedOrderAdmin)