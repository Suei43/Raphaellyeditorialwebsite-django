from django.db import models
from datetime import datetime

class Blog(models.Model):
    title=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default='Faith')
    header=models.CharField(max_length=50, blank=True)
    description=models.TextField(blank=True,default='..click to read!')
    article_paragraph_1=models.TextField(blank=True)
    article_paragraph_2=models.TextField(blank=True)
    article_paragraph_3=models.TextField(blank=True)
    article_paragraph_4=models.TextField(blank=True)
    article_paragraph_5=models.TextField(blank=True)
    article_bible_verse_1=models.TextField(blank=True)
    article_bible_verse_1_passage=models.CharField(max_length=50, blank='True')
    article_bible_verse_2=models.TextField(blank=True)
    article_bible_verse_2_passage=models.CharField(max_length=50, blank='True')
    upload_date=models.DateField(default=datetime.now,blank=True)
    read_time=models.IntegerField()
    picture=models.ImageField(upload_to='photos/')
    def __str__(self):
        return self.title

