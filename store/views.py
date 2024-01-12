from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.

def item_list(request):
    Items = Item.objects.all()
    return render(request, "store/home.html", {"items":Items})


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'store/item_detail.html', {'item': item})