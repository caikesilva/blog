from django.urls import path
from blog.views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView
from django.conf.urls.static import static
from configuracoes import settings

urlpatterns = [
    path('posts/', PostListView.as_view(), name="post_list_view"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post_detail_view"),
    path('posts/new', PostCreateView.as_view(), name="post_new_view"),
    path('posts/update/<int:pk>', PostUpdateView.as_view(), name="post_update_view"),
    path('posts/delete/<int:pk>', PostDeleteView.as_view(), name="post_delete_view"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)