from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):

    class meta:
        model = Post
        fields = ('author', 'title', 'text', 'img', 'created_date', 'published_date')
        widgets = {
            'created_date': forms.DateTimeField(attrs={'type': 'date'}),
            'published_date': forms.DateTimeField(attrs={'type': 'date'}),
        }