from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
class User(AbstractBaseUser):
    full_name = models.CharField(max_length=80)
    email = models.CharField(max_length=120,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    objects = UserManager()
    REQUIRED_FIELDS = ('full_name',)
    USERNAME_FIELD = 'email'
    
    def has_perm(self,perm, obj=None):
        return True
    

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.is_admin
    def __str__(self):
        return self.email
