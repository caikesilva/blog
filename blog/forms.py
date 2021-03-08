from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):

    class meta:
        model = Post
        fields = ('author', 'title', 'text', 'img')
        widgets = {
            'author': forms.SelectMultiple(attrs={ 'class': 'form-control'}),
            'title': forms.TextInput(attrs={ 'class': 'form-control'}),
            'text': forms.TextInput(attrs={ 'class': 'form-control'}),
            'img': forms.FileInput(attrs={ 'class': 'form-control'})
        }