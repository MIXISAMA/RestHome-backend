from django.contrib import admin
from all.models import Company

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tp', "telephone", "address")

