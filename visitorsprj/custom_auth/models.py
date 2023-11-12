from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    class Meta:
        app_label = 'custom_auth'
        
    is_admin = models.BooleanField('Admin', default=False)
    is_staff = models.BooleanField('Staff', default=False)