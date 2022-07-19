from django.contrib import admin
from django.urls import path, include

API_URL = 'api/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('{}account/'.format(API_URL), include('rules.urls')),
    path('{}clients/'.format(API_URL), include('clients.urls')),
]
