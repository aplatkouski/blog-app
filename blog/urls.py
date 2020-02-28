from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:post_pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:post_pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:post_pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:post_pk>/add_comment/', views.add_comment, name='add_comment_to_post'),
]
