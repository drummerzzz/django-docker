from django.urls import path
from accounts.users.views import login_user

urlpatterns = [
    path('login_user/<int:pk>/', login_user, name='login_user')
]
