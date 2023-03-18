from django.shortcuts import render
from .models import Blog
import random

def index(request):
    blogs = list(Blog.objects.all())
    blogs_list = random.sample(blogs,4)
    context ={
        'blogs': blogs_list,
    }
    return render(request,'index.html',context) 


