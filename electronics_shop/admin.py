from django.contrib import admin

from .models import Customer, Product, Category, Order



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", 'address']

    
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]
    
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ["name"]
    
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["title"]





