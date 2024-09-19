from django.urls import path
from .views import BlogListCreateView, BlogDetailView, UserProfileDetailView, CommentCreateView, UserBlogView,SignUpView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('profile/<int:pk>/blogs/', UserProfileDetailView.as_view(), name='user-blogs'),
    path('blogs/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('my-blogs/', UserBlogView.as_view(), name='my-blogs'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
