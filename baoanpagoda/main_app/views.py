from django.shortcuts import render
from .models import ImageLanding, Menu, SubMenu
from gallery.models import GalleryCategories
from collections import defaultdict


# Create your views here.
def index(request):
    imagelanding = ImageLanding.objects.latest('created_at')
    context = {
        'imagelanding': imagelanding,
    }
    return render(request, 'main_app/index.html', context=context)


def menu_views(request):
    about_us = Menu.objects.filter(en_slug='about-us').first()
    action = Menu.objects.filter(en_slug='action').first()
    gallery_categories = GalleryCategories.objects.all()

    # Create a list of dictionaries where each dictionary represents a menu and its associated submenus
    context = {
        'about_us': about_us,
        'action': action,
        'gallery_categories': gallery_categories
    }
    return {'about_us': about_us, 'action': action, 'gallery_categories': gallery_categories}
