# Generated by Django 4.2.5 on 2023-10-09 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagegallery',
            name='category',
        ),
        migrations.RemoveField(
            model_name='mediagallery',
            name='category',
        ),
        migrations.DeleteModel(
            name='GalleryCategories',
        ),
    ]
