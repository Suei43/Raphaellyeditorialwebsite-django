from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>',views.blog,name='blog'),
    path('random',views.randomBlog,name='randomblog'),
]