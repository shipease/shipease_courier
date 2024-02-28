"""custom user model inherited from AbstractUser"""

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import ( BaseUserManager)
 
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where contact_number is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, contact_number, password, **extra_fields):
        """
        Create and save a user with the given mobile and password.
        """
        if not contact_number:
            raise ValueError(_("The Contact Number must be set"))
       
        user = self.model(contact_number=contact_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, contact_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given contact number and password.

        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(contact_number, password, **extra_fields)
    

class User(AbstractUser):
    """
    This custom user model for enhanced func.
    """
    username = None
    contact_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    image = models.URLField(null=True,blank=True)
    user_department = models.CharField(max_length=10)
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    otp=models.CharField(max_length=10,null=True,blank=True)
    is_otp_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    send_whatsapp_update = models.BooleanField(default=True, help_text="Send me Whatsapp updates")
    user_permissions = None
    groups = None

    USERNAME_FIELD = "contact_number"

    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()


    class Meta:
        managed = False
        db_table = "user"
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
 

    def __str__(self):
       return self.contact_number    
