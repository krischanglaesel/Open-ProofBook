# -*- coding: utf-8 -*-
from django import forms

class CreateAlbumForm(forms.Form):
    title = forms.CharField(max_length=60, label='Album Title?')
    #owner = forms.ForeignKey(User, label='Album Owner')
    public = forms.BooleanField(label='Make Album Public?')
    folder = forms.CharField(max_length=60, label='Name of Folder in Albums Directory?')
