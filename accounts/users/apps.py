from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'accounts.users'

    def ready(self):
        import accounts.users.signals
