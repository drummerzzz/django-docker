from django.urls import reverse_lazy


AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = reverse_lazy('users:redirect')
LOGOUT_REDIRECT_URL = reverse_lazy('users:redirect')

ADMINS = [('João', 'jf.interatividade@gmail.com')]
