from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_date')
    list_display_links = ('id', 'title')
    list_per_page = 20
admin.site.register(Blog,BlogAdmin)
