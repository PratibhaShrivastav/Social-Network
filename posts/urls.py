from django.urls import path,re_path
from posts.views import PostList,UserPosts,PostDetail,CreatePost,DeletePost,UpdatePost,AddComment,DeleteComment

app_name='posts'

urlpatterns = [
    path('',PostList.as_view(),name='all'),
    path('new/',CreatePost.as_view(),name='create'),
    re_path(r'by/(?P<username>[-\w]+)/$',UserPosts.as_view(),name='for_user'),
    re_path(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',PostDetail.as_view(),name='single'),
    re_path(r'delete/(?P<pk>\d+)/$',DeletePost.as_view(),name='delete'),
    re_path(r'edit/(?P<pk>\d+)/$',UpdatePost.as_view(),name='edit'),
    re_path(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/comment/$',AddComment.as_view(),name='addcomment'),
    re_path(r'by/(?P<username>[-\w]+)/(?P<postpk>\d+)/comment/(?P<pk>\d+)/delete/$',DeleteComment.as_view(),name='deletecomment'),
]
