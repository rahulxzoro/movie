from django.db import models

# Create your models here.
class Movie(models.Model):
    
    movie_name=models.CharField(max_length=200)
    rating=models.CharField(max_length=200)
    
    banner=models.ImageField(upload_to='pics')
    poster=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=200)
    rating=models.CharField(max_length=200)
    screen=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    duration=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    
    
    def __str__(self):
        
        return self.name
    