# -*- coding: utf-8 -*-
# Create your views here.
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import render_to_response
from open_proofbook.proofbook.models import Album
from open_proofbook.proofbook.forms import CreateAlbumForm
import os


def home(request):
  return HttpResponse("Home")

def create_album(request):
  staff_only(request)
  #if request.method == 'GET':
   # render_to_response(create_album.html)
  
  if request.method == 'POST':
    pass
  else:
    form = CreateAlbumForm()
    return render_to_response('form.html',{'form': form})
      
def album(request, album, page=1):
  owner_only(request, album)
  try:
    a = Album.objects.get(path=album)
  except Album.DoesNotExist:
    return HttpResponseNotFound()
  album_path = settings.STATIC_DOC_ROOT + '/albums/' + album
  pic_list = os.listdir(album_path) 
  pic_list = sorted(pic_list)
  pic_max = (page * 9)
  if pic_max >= len(pic_list):
    pic_max = len(pic_list) - 1
    pic_min = 0
  else:
    pic_min = pic_max - 9
  payload = {
    'title': a.title,
    'user': request.user.first_name + ' ' + request.user.last_name,
    'public': a.public,
    'pic_list': pic_list[pic_min:pic_max],
    'album_dir': '/static/albums/' + album + '/'
    }
  return render_to_response('album.html', payload)

def album_edit(request, album):
  staff_only(request)
  
#Aux

def staff_only(request):
  if (request.user.is_authenticated() == False):
    return HttpResponseRedirect('/accounts/login')
  if (request.user.is_staff == False & user.is_athenticated()):
    return HttpResponseForbidden()
def owner_only(request, album):
  if (request.user.is_authenticated() == False):
    return HttpResponseRedirect('/accounts/login')
  try:
    a = Album.objects.get(path=album)
  except Album.DoesNotExist:
    return HttpResponseNotFound()
  if (a.public == False &  request.user.is_staff == False): #a.owner != request.user &
    return HttpResponseForbidden()
    