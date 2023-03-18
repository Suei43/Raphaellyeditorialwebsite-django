from django.shortcuts import render,get_object_or_404
from main import models
import random


blogs_list = list(models.Blog.objects.all())

def blog(request,id):
    num = 4
    blogs = random.sample(blogs_list,num)
    current_blog = get_object_or_404(models.Blog, pk=id)
    context = {
        'current_blog':current_blog,
        'blogs':blogs,
        'blogs_list':blogs_list
    }
    return render(request,'blogs/blog.html',context)

def randomBlog(request):
    blogs_list = list(models.Blog.objects.all())
    current_blog = random.choice(blogs_list)
    context={
        'current_blog':current_blog,
        'blogs_list':blogs_list
    }
    return render(request,'blogs/blog.html',context)
