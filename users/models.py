from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    user_type = models.CharField(max_length=50, blank=True, null=True,choices=(('admin','admin'),('client','client')))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["last_name"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    @classmethod
    def create_client(cls, first_name, last_name, email, phone_number, id_number):
        password = f'{id_number}{last_name}'
        user = cls(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, user_type='client')
        user.set_password(password)
        user.save()
        return user

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.is_verified = True
            self.is_active = True
        super(User, self).save(*args, **kwargs)
