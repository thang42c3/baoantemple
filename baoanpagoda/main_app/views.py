from django.shortcuts import render
from . models import ImageLanding, AboutUsCategory


# Create your views here.
def index(request):
    imagelanding = ImageLanding.objects.latest('created_at')
    aboutUsCategories = AboutUsCategory.objects.all()
    context = {'imagelanding': imagelanding,
               'aboutUsCategories': aboutUsCategories}
    return render(request, 'main_app/index.html', context=context)