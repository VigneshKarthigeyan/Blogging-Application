from django.urls import path
from .views import *


urlpatterns = [
    # path('', index,name='starting-page'),
    path('', Index.as_view(),name='starting-page'),
    path('posts', AllPosts.as_view(),name='posts-page'),
    path('read-later', ReadLaterView.as_view(),name='read-later'),
    path('posts/<slug:slug>', SinglePost.as_view(),name='post-detail-page')
]
