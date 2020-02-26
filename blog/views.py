from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect, Http404

from .models import Post


def post_list(request):
	posts = Post.objects.order_by('published_date')[:10]
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_pk):
	post = get_object_or_404(Post, pk=post_pk)
	return render(request, 'blog/post_detail.html', {'post': post})
