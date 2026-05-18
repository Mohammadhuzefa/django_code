from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import EmployeeProfile

@admin.register(EmployeeProfile)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'phone') # Admin panel mein ye columns dikhenge
    search_fields = ('city', 'user__username')