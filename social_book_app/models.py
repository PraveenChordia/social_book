from email.policy import default
from operator import mod
from secrets import choice
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Permission
from django.utils.itercompat import is_iterable
from django.utils.translation import gettext_lazy as _
from .manager import UserManager


# Create your models here.
class UserDetails(AbstractBaseUser, PermissionsMixin):
    acc_type = [
        ('Author', 'Author'),
        ('Seller', 'Seller')
    ]
    username = models.CharField(verbose_name='Pen Name', max_length=12, primary_key=True)
    email = models.EmailField(verbose_name='Email', max_length=127)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    public_visibility = models.BooleanField(verbose_name='Public Visibility', default=False)
    dob = models.DateField(verbose_name='Date of Birth', null=True)
    age = models.IntegerField(verbose_name='Age', null=True)
    account_type = models.CharField(verbose_name='Account Type', max_length=10, choices=acc_type, null=True)
    address = models.TextField(_('Address'), max_length=1000, null=True)
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    about = models.TextField(_('about'), max_length=1000, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    EMAIL_FIELD = 'email'
    objects = UserManager()

    class META:
        db_table = 'User'

    def __str__(self):
        return self.username

    def has_perms(self, perm_list, obj=None):
        if not is_iterable(perm_list) or isinstance(perm_list, str):
            raise ValueError('perm_list must be an iterable of permissions.')
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_lable):
        return True