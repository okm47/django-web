from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

context = {
    "post": Post.objects.all()

}


def home(request):
    return render(request, 'blog/home.html', context)
