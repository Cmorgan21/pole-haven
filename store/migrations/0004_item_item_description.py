# Generated by Django 4.2.9 on 2024-01-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_item_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_description',
            field=models.TextField(default='text'),
            preserve_default=False,
        ),
    ]