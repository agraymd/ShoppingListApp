from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryItem
from .forms import add_grocery_item

# Create your views here.


def index(request):
    return HttpResponse("Suck mah nutz")

# List Shopping Items in a View


def shopping_list_view(request):
    grocery_objects = GroceryItem.objects.all()
    if request.method == "POST":
        form = add_grocery_item(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
    else:
        form = add_grocery_item()
    context = {
        'grocery_objects': grocery_objects,
        'form': form,
    }
    return render(request, "grocery_items/index.html", context)


