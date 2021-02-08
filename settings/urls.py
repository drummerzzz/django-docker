from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.users.urls')),
    path('api', include('app.api.urls')),
    path('accounts/admin/', admin.site.urls),
]
