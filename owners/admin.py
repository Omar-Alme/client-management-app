from django.contrib import admin
from .models import Owner


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'first_name',
        'last_name', 'email',
        'business_name'
        )
    list_filter = (
        'user', 'first_name',
        'last_name', 'email',
        'business_name'
        )
    search_fields = (
        'user',
        'first_name',
        'last_name',
        'email',
        'business_name'
        )
    ordering = ('user', 'first_name', 'last_name', 'email', 'business_name')
