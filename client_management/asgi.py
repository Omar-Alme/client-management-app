"""ASGI config for client_management project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'client_management.settings')

application = get_asgi_application()
