from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Item, Order, OrderItem


# Create your views here.

def item_list(request):
    Items = Item.objects.all()
    return render(request, "store/home.html", {"items":Items})


def item_detail(request, slug):
    item = get_object_or_404(Item, slug=slug)
    return render(request, 'store/item_detail.html', {'item': item})

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
    
    # Redirect to item_detail with the correct slug parameter
    return redirect("store:item_detail", slug=slug)

def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("store:item_detail", slug=slug)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("store:item_detail", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("store:item_detail", slug=slug)

def order_summary(request):
    orders = Order.objects.filter(user=request.user, ordered=False)

    # Calculate total order price, you can customize this based on your model structure
    total_price = sum(order.get_total() for order in orders)

    return render(request, 'store/order_summary.html', {'orders': orders,
        'total_price': total_price,} )

def store_view(request):
    Items = Item.objects.all()
    return render(request, 'store/online_store.html', {"items":Items})