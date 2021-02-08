from django.urls import path
from accounts.users.views import login_user, login_redirect

app_name = 'users'

urlpatterns = [
    path('', login_redirect, name='redirect'),
    path('login_user/<int:pk>/', login_user, name='login_user')
]
