# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    #Title of category, display on category bar.
    title = models.CharField(max_length=60)
    
    def __unicode__(self):
        return self.title
    
#Not fully implemented yet. Basically does nothing. Will hold settings per site.
class Site(models.Model):
    title = models.CharField(max_length=254, help_text="Title of the site")
    pics_per_page = models.IntegerField(help_text="Number of pictures showed per page in the album. Default is 8.")
    domain_name = models.CharField(max_length=254, help_text="Domain name of the site")
    
    def __unicode__(self):
        return self.title  
    
class Album(models.Model):
    # Title at top of album. Folder is built from this.
    title = models.CharField(max_length=60, help_text="Title of the album")
    # Only owner and staff can view if not public.
    owner = models.ForeignKey(User, help_text="Set this to your user name, for now.")
    # Whether any user can see or not, and will appear on homepage.
    public = models.BooleanField(help_text="Whether this album is publicly viewable or not")
    # URL to album e.g. '/Test_Album'.
    path = models.CharField(max_length=70, help_text="The case sensitive name of the album folder you created via FTP. E.g. 'personal' or 'firstname_lastname'")
    # Assign thumbnail picture, or one will be assigned for you.
    thumbnail = models.CharField(max_length=70, help_text="Name of the image you want displayed on the main page. E.g. photo.jpg")
    # Password for access to album, and to share with friends/family
    password = models.CharField(max_length=20, help_text="Simple password to access the site. Not used yet.")
    # Date pictures were taken
    date = models.DateTimeField(help_text="Date of the photoshoot. Album will not be accessible after one year.")
    # Category of the album
    category = models.ForeignKey(Category, help_text="Category of the album. E.g. Wedding, Senior Pics, etc")
    
    def __unicode__(self):
        return self.title
      
class Image(db.Model):
  
