from django.contrib import admin
from root.models import Root

# Register your models here.

@admin.register(Root)
class RootAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', "telephone")
    list_display_links = ('username', 'first_name')
