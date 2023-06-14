from django.shortcuts import render
from .models import Photos
from django.http import HttpResponse

# Create your views here.
def photos_list(request):
    photos = Photos.objects.all()
    context = {'photos': photos}
    return render (request, "photos.html", context)

