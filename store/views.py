from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from .models import Item, Order, OrderItem, ITEM_CATEGORY
from blog.models import Post
from .forms import ContactForm


# Create your views here.

def item_list(request):
    latest_blog_posts = Post.objects.filter(status=1).order_by('-created_on')[:3]
    Items = Item.objects.all()
    return render(request, "store/home.html", {"items": Items, 'latest_blog_posts': latest_blog_posts})


def item_detail(request, slug):

    item = get_object_or_404(Item, slug=slug)
    related_items = Item.objects.filter(category=item.category).exclude(slug=item.slug).order_by('?')[:4]
    return render(request, 'store/item_detail.html', {'item': item, 'related_items': related_items})


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    quantity = int(request.POST.get('quantity', 1))

    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )

    if not created:
        order_item.quantity += quantity
        order_item.save()
        messages.info(request, f"{quantity} {item.title}(s) added to your cart.")
    else:
        order_item.quantity = quantity
        order_item.save()

        order_qs = Order.objects.filter(user=request.user, ordered=False)

        if order_qs.exists():
            order = order_qs[0]
            order.items.add(order_item)
            messages.info(request, f"{quantity} {item.title}(s) added to your cart.")
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(
                user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            messages.info(request, f"{quantity} {item.title}(s) added to your cart.")

    return redirect("store:item_detail", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        order_item = OrderItem.objects.filter(
            item=item,
            user=request.user,
            ordered=False
        ).first()

        if order_item:
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")

            if order.items.count() == 0:
                order.ordered = True
                order.save()

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

    return render(request, 'store/order_summary.html', {'orders': orders, 'total_price': total_price})


def store_view(request):
    category_filter = request.GET.get('category')
    items = Item.objects.all()

    # Include ITEM_CATEGORY in the context
    categories = ITEM_CATEGORY

    if category_filter:
        items = items.filter(category=category_filter)

    return render(request, 'store/online_store.html', {'items': items, 'categories': categories})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            email_message = f"Pole Haven Support:\nName: {name}\nEmail: {email}\nSubject: {subject}\n\n{message}"

            send_mail(
                'Pole Haven Contact Form',
                email_message,
                'callummorgan666@gmail.com',
                [email],
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent! We will get in touch with you shortly.')

            return redirect('store:contact_success')

    else:
        form = ContactForm()

    return render(request, 'store/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'store/contact_success.html')
