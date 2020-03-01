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
    path('post/<int:post_pk>/comment/add/', views.add_comment, name='add_comment_to_post'),
    path('post/<int:post_pk>/comment/<int:comment_pk>/approve/', views.comment_approve, name='comment_approve'),
    path('post/<int:post_pk>/comment/<int:comment_pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<int:post_pk>/choice/new/', views.choice_new, name='choice_new'),
    path('post/<int:post_pk>/vote/', views.choice_vote, name='choice_vote'),
    path('post/<int:post_pk>/choice/<int:choice_pk>/remove/', views.choice_remove, name='choice_remove'),
]
