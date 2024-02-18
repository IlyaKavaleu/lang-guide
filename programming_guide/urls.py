"""
URL configuration for programming_guide project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from orders.views import stripe_webhook_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('languages.urls', 'languages')),
    path('users/', include('users.urls', 'users')),
    path('comments/', include('comments.urls', 'comments')),
    path('basket/', include('basket.urls', 'basket')),
    path('opinions/', include('opinions.urls', 'opinions')),
    path('chat/', include('chat.urls', 'chat')),
    path('paid_lessons/', include('paid_lessons.urls', 'paid_lessons')),
    path('paid_card/', include('paid_card.urls', 'paid_card')),
    path('orders/', include('orders.urls', 'orders')),
    path('webhook/stripe/', stripe_webhook_view, name='stripe_webhook'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
