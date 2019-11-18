from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField()
    #poster = models.models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #user  = 

    
    