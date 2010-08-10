# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
  
  def __unicode__(self):
    return self.title