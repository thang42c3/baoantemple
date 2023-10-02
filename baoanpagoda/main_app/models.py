from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class ImageLanding(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='imagine/')
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-imagelanding', args=[self.slug])


class AboutUsCategory(models.Model):
    vn_name = models.CharField(max_length=255)
    vn_slug = models.SlugField(max_length=250)
    en_name = models.CharField(max_length=255)
    en_slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.en_name

    def get_absolute_vn_url(self):
        return reverse('vn_about_us_category', args=[self.vn_slug])

    def get_absolute_en_url(self):
        return reverse('en_about_us_category', args=[self.en_slug])


