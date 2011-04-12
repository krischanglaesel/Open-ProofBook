# -*- coding: utf-8 -*-
from google.appengine.ext import db

# Create your db here.

class Category(db.Model):
    #Title of category, display on category bar.
    title = db.StringProperty()
    
    def __unicode__(self):
        return self.title
    
#Not fully implemented yet. Basically does nothing. Will hold settings per site.
class Site(db.Model):
    title = db.StringProperty(required=True)
    pics_per_page = db.IntegerProperty(required=True)
    domain_name = db.StringProperty(required=True)
    
    def __unicode__(self):
        return self.title  
    
class Album(db.Model):
    # Title at top of album. Folder is built from this.
    title = db.StringProperty(required=True)
    # Whether any user can see or not, and will appear on homepage.
    public = db.BooleanProperty(required=True)
    # Assign thumbnail picture, or one will be assigned for you.
    thumbnail = db.StringProperty(required=True)
    # Password for access to album, and to share with friends/family.
    password = db.StringProperty(required=True)
    # Date pictures were taken.
    date = db.DateTimeProperty(required=True)
    # Category of the album.
    category = db.ReferenceProperty(Category, required=True)
    
    def __unicode__(self):
        return self.title
      
class Image(db.Model):
	# Name of the image.
	name = db.StringProperty(required=True)
	# Which album to display the image in.
	album = db.ReferenceProperty(Album, required=True)
	# Image file
	image = db.BlobProperty(required=True)
	# Generated thumbnail
	thumbnail = db.BlobProperty()

	def __unicode__(self):
		return self.name
  
