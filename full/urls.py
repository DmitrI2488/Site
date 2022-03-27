import django.contrib.auth.urls
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('django.contrib.auth.urls')),
    path('', include('members.urls')),
    path('', include('HomePage.urls')),
    path('', include('events.urls')),
]
