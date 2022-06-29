from socket import fromshare
from django import forms
from .models import Post

#create our forms
class PostForms(forms.ModelForm):
    #create a meta class What is a meta class?
    class Meta:
        model=Post
        fields=[
            'title',
            'author',
            'body', 
            'status', 
            'created', 
            'updated',
        ]