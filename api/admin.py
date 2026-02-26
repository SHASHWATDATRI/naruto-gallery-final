from django.contrib import admin

#v Register your models here.
from django.contrib import admin
from .models import Artwork

# Isse Artworks admin panel mein dikhne lagenge
admin.site.register(Artwork)
