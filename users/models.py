# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from . import managers


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.email


class Profile(models.Model):
    # Relations
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
        verbose_name=_("User"),
        on_delete=models.CASCADE,
    )
    # Attributes - Mandatory
    interaction = models.PositiveIntegerField(
        default=0,
        verbose_name=_("interaction")
    )
    # Attributes - Optional
    # Object Manager
    objects = managers.ProfileManager()

    # Custom Properties
    @property
    def username(self):
        return self.user.username
    first_name = models.CharField('First Name', max_length=64, null=True, blank=True, default='',)
    last_name = models.CharField('Last Name', max_length=64, null=True, blank=True, default='',)

    # Meta and String
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ('user',)

    # Methods
    def get_absolute_url(self):
        return reverse('settings',)
        # return reverse('settings', kwargs={'pk': self.pk})

    def __str__(self):
        return self.user.username
