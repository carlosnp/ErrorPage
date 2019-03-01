"""errorpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import django
from django.contrib import admin
from django.urls import path, include
# Configuracion de los archivos estaticos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace="users")),
    path('400/',  django.views.defaults.bad_request, kwargs={'exception': Exception('Bad Request!')},name='Error400'),
    path('403/',  django.views.defaults.permission_denied, kwargs={'exception': Exception('Permission Denied!')},name='Error403'),
    path('404/',  django.views.defaults.page_not_found, kwargs={'exception': Exception('Page Not Found!')},name='Error404'),
    path('500/',  django.views.defaults.server_error, name='Error500'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)