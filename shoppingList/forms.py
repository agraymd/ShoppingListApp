from django import forms
from .models import GroceryItem

class add_grocery_item(forms.ModelForm):
    

    class Meta:
        model = GroceryItem
        fields = ('item_name',)
