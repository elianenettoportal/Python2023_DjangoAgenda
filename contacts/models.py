from django.db import models
from django.utils import timezone


class Category(models.Model):
    name      = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name      = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    phone     = models.CharField(max_length=255)
    email     = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category    = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    show_contact = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    pic = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')

    def __str__(self):
        return self.name +' '+ self.last_name +' '+self.email +' '+self.category.name



