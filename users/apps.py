from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UsersConfig(AppConfig):
    name = 'users'


class ProfilesConfig(AppConfig):
    name = 'users'
    verbose_name = _('users.profile')

    def ready(self):
        import users.signals  # noqa
