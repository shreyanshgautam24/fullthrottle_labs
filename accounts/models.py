# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self,real_id,password, **extra_fields):
        if not real_id:
            raise ValueError("Users must have an ID")
        user = self.model(
        real_id =real_id,**extra_fields
        )
        user.set_password(password)
        user.save(using= self._db)
        return user

    def create_user(self,real_id,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(real_id,password,**extra_fields)

    def create_superuser(self,real_id,password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser Must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser Must have is_superuser=True.')

        return self._create_user(real_id,password,**extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    real_id = models.CharField(max_length =100, null = False,unique = True)
    real_name = models.CharField(max_length =100, null = True)
    time_zone = models.CharField(max_length =100, null = True)
    is_staff = models.BooleanField(
        _('staff status'),
        default= False,
        help_text=_('designates whether the user can log into this sdmin site')
    )
    objects = UserManager()
    USERNAME_FIELD = 'real_id'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = ['user']
        verbose_name_plural = ['users']
        swappable = 'AUTH_USER_MODEL'
    def __str__(self):
        return self.real_name
    def get_short_name(self):
        return self.real_name

class ActivityPeriod(models.Model):
    start_time = models.DateTimeField(auto_now_add=False)
    end_time = models.DateTimeField(auto_now_add=False)
    user = models.ForeignKey(User, null = False , related_name = 'activityUser')
