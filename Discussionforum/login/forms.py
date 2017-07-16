'''
Created on 16-Jul-2017

@author: Sanjana
'''
from django import forms

from .models import discussion
from .models import comment

class PostForm(forms.ModelForm):

    class Meta:
        model = discussion
        fields = ('subject',)
        
        
class commentForm(forms.ModelForm):

    class Meta:
        model = comment
        fields = ('content',)