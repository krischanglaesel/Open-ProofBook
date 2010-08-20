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
  title = models.CharField(max_length=254)
  pics_per_page = models.IntegerField()
  domain_name = models.CharField(max_length=254)
  
  def __unicode__(self):
    return self.title  
    
class Album(models.Model):
  # Title at top of album. Folder is built from this.
  title = models.CharField(max_length=60)
  # Only owner and staff can view if not public.
  owner = models.ForeignKey(User)
  # Whether any user can see or not, and will appear on homepage.
  public = models.BooleanField()
  # URL to album e.g. '/Test_Album'.
  path = models.CharField(max_length=70)
  # Assign thumbnail picture, or one will be assigned for you.
  thumbnail = models.CharField(max_length=70)
  # Password for access to album, and to share with friends/family
  password = models.CharField(max_length=20)
  # Date pictures were taken
  date = models.DateTimeField()
  # Category of the album
  category = models.ForeignKey(Category)
  
  def __unicode__(self):
    return self.title
    