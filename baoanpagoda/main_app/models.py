from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class ImageLanding(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True, null=True, help_text="You can use HTML tags for styling.")
    image = models.ImageField(upload_to='imagine/')
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-imagelanding', args=[self.slug])


class Menu(models.Model):
    vn_name = models.CharField(max_length=255)
    vn_slug = models.SlugField(max_length=250)
    en_name = models.CharField(max_length=255)
    en_slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='imagine/', blank=True)

    def __str__(self):
        return self.en_name

    def get_absolute_vn_url(self):
        return reverse('vn_menu_category', args=[self.vn_slug])

    def get_absolute_en_url(self):
        return reverse('en_menu_category', args=[self.en_slug])


class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, related_name='submenu', on_delete=models.CASCADE, null=True)
    vn_name = models.CharField(max_length=255)
    vn_slug = models.SlugField(max_length=250)
    en_name = models.CharField(max_length=255)
    en_slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='imagine/', blank=True)

    def __str__(self):
        return self.en_name

    def get_absolute_vn_url(self):
        return reverse('vn_about_us_category', args=[self.vn_slug])

    def get_absolute_en_url(self):
        return reverse('en_about_us_category', args=[self.en_slug])





