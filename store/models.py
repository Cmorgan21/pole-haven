from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from cloudinary.models import CloudinaryField


# Create your models here.
ITEM_CATEGORY = (
    ('CL', 'Clothes'),
    ('GR', 'Grip'),
    ('ACC', 'Accessories')
)


class Item(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=ITEM_CATEGORY, max_length=3)
    item_description = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("store:item_detail", kwargs={
            'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse("store:add-to-cart", kwargs={
            'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse("store:remove-from-cart", kwargs={
            'slug': self.slug})

    def get_category_display_name(self):
        # Get the display name for the category
        return dict(ITEM_CATEGORY)[self.category]

    def savings(self):
        if self.discount_price:
            return self.price - self.discount_price

    def __str__(self):
        return f"Comment {self.title} | {self.category} | {self.item_description}"


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_final_price(self):
        if self.item.discount_price:
            return self.quantity * self.item.discount_price
        return self.quantity * self.item.price


class Order(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}'s order {self.ordered_date}"

    def get_total(self):
        return sum(item.get_final_price() for item in self.items.all())
