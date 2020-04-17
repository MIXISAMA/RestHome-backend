from django.contrib import admin
from old.models import Old

# Register your models here.

@admin.register(Old)
class OldAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'sex', "birthday", "telephone", "address")
    list_display_links = ('username', 'name')
    list_filter = ('sex', )
