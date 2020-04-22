from django.shortcuts import render


# Create your views here.

# List Shopping Items in a View


def shopping_list_view(request):

    return render(request, "grocery_items/index.html")


