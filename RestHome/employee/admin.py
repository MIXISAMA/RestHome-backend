from datetime import date

from django.contrib import admin
from employee.models import Position, Emp, Room, Bill

# Register your models here.

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
    list_display = ('username', 'position', 'first_name', 'sex', "birthday", "telephone", "address")
    list_display_links = ('username', 'first_name')
    list_filter = ('sex', )

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'emp', 'status')

class BillMonthFilter(admin.SimpleListFilter):
    title = "月份"
    parameter_name = "month"

    def lookups(self, request, model_admin):
        for i in range(1, 13):
            yield (i, i)

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(date__month=self.value())

class BillYearFilter(admin.SimpleListFilter):
    title = "年度"
    parameter_name = "year"

    def lookups(self, request, model_admin):
        for i in range(2018, date.today().year+1):
            yield(i, i)

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(date__year=self.value())

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'emp', 'date', 'money')
    list_filter = (BillYearFilter, BillMonthFilter, 'emp')
