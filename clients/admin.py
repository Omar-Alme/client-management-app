from django.contrib import admin
from .models import Client, Owner
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Client)
class clientAdmin(SummernoteModelAdmin):
    summernote_fields = ('notes',)
    list_display = ('client_name', 'email', 'industry', 'user',)
    list_filter = ('user',)
    search_fields = ('client_name', 'industry', 'user', 'email',)