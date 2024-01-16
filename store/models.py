from django.db import models
from django.conf import settings
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

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.title

