from django.contrib import admin
from .models import QuoteModel
# Register your models here.
@admin.register(QuoteModel)
class QuoteModelAdmin(admin.ModelAdmin):
    list_display = ['name','company_name','tel','need_driver_assistence']
    ordering = ['-id']