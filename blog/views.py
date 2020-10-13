from django.shortcuts import render, get_object_or_404 # get_object_or_404 - bierze object from data base or display 404 eror

from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id) #pk - primary key
    return render(request, 'blog/detail.html', {'blog':detailblog})
