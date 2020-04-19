from django import forms
from .models import grocery_item

class add_grocery_item(forms.ModelForm):
    

    class Meta:
        model = grocery_item
        fields = ('item_name',)
