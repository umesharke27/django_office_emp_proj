from django.contrib import admin
from .models import CopperProduct

# Register your models here.

class CopperProductAdmin(admin.ModelAdmin):
    list_display = ['prd_name', 'prd_qnty', 'prd_validity', 'prd_valid_upto']


admin.site.register(CopperProduct, CopperProductAdmin)
