from django.contrib import admin
from .models import Product_details_Model

# Register your models here.

class Product_detail_Admin(admin.ModelAdmin):
    list_display = ['name','prd_qnty','prd_price','prd_loc']
admin.site.register(Product_details_Model,Product_detail_Admin)
