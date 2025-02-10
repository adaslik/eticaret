from django.contrib import admin
from .models import Address, Product, Category, Order, Cart

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'total_price', 'quantity', 'status', 'created_at')
    list_filter = ('status',)

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at', 'updated_at')
    search_fields = ('user', 'product')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'country', 'zip_code')
    search_fields = ('user', 'city', 'country', 'zip_code')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Cart, CartAdmin)


