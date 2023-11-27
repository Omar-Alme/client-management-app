from django.contrib import admin
from .models import Client
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Client)
class clientAdmin(SummernoteModelAdmin):
    summernote_fields = ('notes',)
    list_display = ('client_name', 'email', 'industry', 'online_presence')
    list_filter = ('industry', 'online_presence')
    search_fields = ('client_name', 'industry', 'online_presence')