from django.contrib import admin
from old.models import Old

# Register your models here.

@admin.register(Old)
class OldAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'sex', "birthday", "telephone", "address")
    list_display_links = ('username', 'first_name')
    list_filter = ('sex', )
