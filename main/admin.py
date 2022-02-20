from django.contrib import admin
from .models import QuoteModel,Drivers
# Register your models here.

@admin.register(QuoteModel)
class QuoteModelAdmin(admin.ModelAdmin):
    list_display = ['name','company_name','tel','need_driver_assistence']
    ordering = ['-id']

@admin.register(Drivers)
class DriversModelAdmin(admin.ModelAdmin):
    list_display = ['first_name','phone','driver_license','state']
    ordering = ['-id']
    