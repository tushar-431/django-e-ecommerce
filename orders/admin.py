from django.contrib import admin
from .models import Payment, Order, OrderProduct

# Register your models here.
class OrderrProductInLine(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product','quantity', 'product_price', 'ordered',)
    extra=0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number' ,'full_name', 'phone', 'city', 'order_total', 'tax', 'status', 'is_ordered']
    list_display_links=('tax',)
    list_filter = ['status', 'is_ordered']
    
    search_fields=['order_number', 'first_name', 'last_name', 'phone', 'email', 'tax']
    list_per_page=20
    inlines = [OrderrProductInLine]

admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
