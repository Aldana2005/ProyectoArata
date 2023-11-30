"""
URL configuration for Arata project.

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

from django.contrib import admin
from django.urls import path, include
from Arata_app.auth import urls as auth_urls
from Arata_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(auth_urls)),
    path('', views.inicio, name='inicio'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),

    path('semillas/', views.semilla_list, name='semilla_list'),
    path('home/', views.home, name='home'), 

    path('semilla/new/', views.semilla_new, name='semilla_new'),
    path('semilla/<int:pk>/edit/', views.semilla_edit, name='semilla_edit'),
    path('semilla/<int:pk>/delete/', views.semilla_delete, name='semilla_delete'),
  
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

