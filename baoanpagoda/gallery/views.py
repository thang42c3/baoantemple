from django.shortcuts import render
from . models import ImageGallery, MediaGallery, GalleryCategories
from django.core.paginator import Paginator
# Create your views here.


def list_categories(request):
    image_gallery_list = ImageGallery.objects.all()
    paginator = Paginator(image_gallery_list, 9)
    page = request.GET.get('page')
    image_galleries = paginator.get_page(page)

    media_galleries = MediaGallery.objects.all()
    gallery_categories = GalleryCategories.objects.all()
    return render(request, 'list-category.html', {'image_galleries': image_galleries,
                                                  'media_galleries': media_galleries,
                                                  'gallery_categories': gallery_categories})