# ASGI config for programming_guide project.
# It exposes the ASGI callable as a module-level variable named ``application``.
# For more information on this file, see https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routine import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programming_guide.settings')

# Объединяем две части application в одну
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
