# todo/todo/urls.py : Main urls.py
from django.contrib import admin
from django.urls import path, include
from ai_api import urls as Rocket_Elevators_Django_API_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('todos/', include(Rocket_Elevators_Django_API_urls)),
]