
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# Creating class for Grocery Item object.


class GroceryItem(models.Model):
    item_name = models.CharField(max_length=75, verbose_name="I Need")


    def __str__(self):
        return self.item_name
