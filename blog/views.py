from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from blog.models import Post
from django.shortcuts import get_object_or_404
# Create your views here.

class PostCreateView(CreateView):
    model = Post
    fields = 'author', 'title', 'text','img', 'created_date', 'published_date'
    success_url = "/posts/"  
    template_name = "blog/new_post.html"

class PostListView(ListView):
    model = Post
    paginate_by = 2
    ordering = ['-published_date']
    template_name = "blog/post_list.html"

class PostDetailView(DetailView):
    model = Post
    slug_field = id
    template_name = "blog/post_detail.html"

class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    fields = 'author', 'title', 'text','img','created_date', 'published_date'
    success_url = "/posts/{id}" 

class PostDeleteView(DeleteView):
    model = Post
    slug_field = id
    success_url = "/posts/" 
    template_name = "blog/post_delete.html"
    


