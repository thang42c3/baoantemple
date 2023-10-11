from django.shortcuts import render
from .models import ImageLanding, Menu, SubMenu
from gallery.models import GalleryCategories, ImageGallery, MediaGallery
from action.models import ActionsCategory, Action
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    imagelanding = ImageLanding.objects.latest('created_at')
    image_gallery_list = ImageGallery.objects.all().order_by('created_at')
    paginator = Paginator(image_gallery_list, 6)
    page = request.GET.get('page')
    image_galleries = paginator.get_page(page)

    media_galleries = MediaGallery.objects.all()
    gallery_categories = GalleryCategories.objects.all()

    context = {
        'imagelanding': imagelanding,
        'image_galleries': image_galleries,
        'media_galleries': media_galleries,
        'gallery_categories': gallery_categories,
    }
    return render(request, 'main_app/index.html', context=context)


def menu_views(request):
    about_us = Menu.objects.filter(en_slug='about-us').first()
    action = Menu.objects.filter(en_slug='action').first()
    gallery_categories = GalleryCategories.objects.all()
    action_categories = ActionsCategory.objects.all()

    # Create a list of dictionaries where each dictionary represents a menu and its associated submenus
    context = {
        'about_us': about_us,
        'action': action,
        'gallery_categories': gallery_categories,
        'action_categories': action_categories
    }
    return context
