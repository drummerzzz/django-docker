from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from accounts.users.models import User

@login_required
@user_passes_test(lambda user: user.is_superuser)
def login_user(request, pk):
  user = User.objects.get(pk=pk)
  login(request, user)
  return redirect('/admin')