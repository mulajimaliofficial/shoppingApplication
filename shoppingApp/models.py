from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CommanTime(models.Model):
    created_at = models.DateTimeField("Created Date", auto_now_add=True)
    updated_at = models.DateTimeField("Updated Date", auto_now=True)

    class Meta:
        abstract = True


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Please assign is_staff=True for superuser'))
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                _('Please assign is_superuser=True for superuser'))
        return self.create_user(email, password, **other_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(_('Name'), max_length=150)
    phone_no = models.CharField(_('Phone No'), max_length=15)
    address = models.TextField(_('Address'))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


class Product(CommanTime):
    title = models.CharField("Title", blank=True, null=True, max_length=255)
    description = models.CharField("Description",blank=True,null=True,max_length=255)
    brand = models.CharField("Brand",blank=True,null=True,max_length=255)
    size = models.CharField("Size",blank=True,null=True,max_length=255)
    price = models.PositiveIntegerField("Price",blank=True,null=True)
    image = models.FileField("Image",upload_to ='productimage/%Y/%m/%d/%H/%M/%S')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Product"