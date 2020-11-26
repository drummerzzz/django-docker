from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from accounts.users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
  list_display = ['username', 'first_name', 'last_name', 'is_active', 'authenticate']
  list_filter = ['is_active', 'is_staff', 'groups']
  search_fields = ['username']
  readonly_fields = ['email', 'is_superuser', 
    'is_staff', 'last_login', 'date_joined', 'user_permissions']

  def authenticate(self, obj):
    return mark_safe(f'<a class="mark_safe" href="/login_user/{obj.pk}/">Logar na conta</a>')

  
  def get_queryset(self, request):
    queryset = super().get_queryset(request)
    if request.user.is_superuser:
      return queryset
    return queryset.exclude(is_superuser=True)

  def get_readonly_fields(self, request, obj=None):
    if request.user.is_superuser:
      return ['email']
    return self.readonly_fields