from django.shortcuts import render
from .models import Post, Lead



def index(request):
    data = Post.objects.all()
    return render(request, "index.html", {'post': data})

def about(request):
    data = Post.objects.all()
    return render(request, "about.html", {'post': data})

def galery(request):
    data = Post.objects.all()
    return render(request, "galery.html", {'post': data})

def news(request):
    data = Lead.objects.all()
    return render(request, "news.html", {'lead': data})

def team(request):
    data = Post.objects.all()
    return render(request, "team.html", {'post': data})

def contact(request):
    data = Post.objects.all()
    return render(request, "contact.html", {'post': data})