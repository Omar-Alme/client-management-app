from django.contrib import admin
from .models import client
from django_summernote.admin import SummernoteModelAdmin


@admin.register(client)
class clientAdmin(SummernoteModelAdmin):
    summernote_fields = ('notes',)
    list_display = ('Client_name', 'email', 'industry', 'Online_Presence')
    list_filter = ('industry', 'online_presence')
    search_fields = ('client_name', 'industry', 'online_presence')