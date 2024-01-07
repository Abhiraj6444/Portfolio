from django.shortcuts import render
from .models import Blog

def allbolgs(request):
    blogs = Blog.objects
    return render(request, 'blog/allbolgs.html',{ 'blogs':blogs })