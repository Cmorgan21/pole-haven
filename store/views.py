from django.shortcuts import render
from .models import Item

# Create your views here.

def item_list(request):
    Items = Item.objects.all()
    return render(request, "store/item_list.html", {"Items":Items})
