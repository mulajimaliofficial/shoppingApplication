from django.db import models

# Create your models here.
class CommanTime(models.Model):
    created_at = models.DateTimeField("Created Date", auto_now_add=True)
    updated_at = models.DateTimeField("Updated Date", auto_now=True)

    class Meta:
        abstract = True

class Product(CommanTime):
    title = models.CharField("Title", blank=True, null=True, max_length=255)
    description = models.CharField("Description",blank=True,null=True,max_length=255)
    brand = models.CharField("Brand",blank=True,null=True,max_length=255)
    size = models.CharField("Size",blank=True,null=True,max_length=255)
    price = models.PositiveIntegerField("Price",blank=True,null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Product"