from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from travels.user_manager import CustomUserManager
from enum import Enum


class CategoryTypes(Enum):
    no_iniciado = 0
    en_curso = 1
    completado = 2
    cancelado = 3

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class User(AbstractUser):
    username = None
    last_login = None
    password = models.CharField(
        _('password'), max_length=128,
        blank=True, null=True
    )
    objects = CustomUserManager()
    email = models.EmailField(_('email address'), unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class Category(models.Model):
    name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Travel(models.Model):
    user = models.ForeignKey(User, related_name='travel_user', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='travel_user', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, default=0, choices=CategoryTypes.choices())
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
