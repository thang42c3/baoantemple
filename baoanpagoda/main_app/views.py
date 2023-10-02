from django.shortcuts import render
from . models import ImageLanding


# Create your views here.
def index(request):
    imagelanding = ImageLanding.objects.latest('created_at')
    context = {'imagelanding': imagelanding,}
    return render(request, 'main_app/index.html', context=context)