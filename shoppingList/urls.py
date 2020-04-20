from django.urls import path
from . import views


urlpatterns = [
    path('', views.shopping_list_view, name="shoppinglistview"),
    ]
