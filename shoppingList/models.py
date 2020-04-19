from django.db import models

# Create your models here.

#Creating class for Grocey Item object.
class grocery_item(models.Model):
    item_name = models.CharField(max_length=75)

    def __str__(self):
        return self.item_name
