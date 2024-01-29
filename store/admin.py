from django.contrib import admin
from .models import Item, OrderItem, Order

# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'discount_price')
    search_fields = ('title', 'category')
    list_filter = ('category',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity', 'ordered', 'get_final_price')
    list_filter = ('ordered',)
    search_fields = ('item__title',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'ordered_date', 'get_total', 'ordered')
    list_filter = ('ordered',)
    search_fields = ('user__username',)