from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_list(request):
	posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_pk):
	post = get_object_or_404(Post, pk=post_pk)
	comments = post.get_comments(request.user.is_authenticated)
	return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})


@login_required
def post_edit(request, post_pk):
	post = get_object_or_404(Post, pk=post_pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', post_pk=post_pk)
	form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', post_pk=post.pk)
	form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
	return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, post_pk):
	post = get_object_or_404(Post, pk=post_pk)
	post.publish()
	return redirect('post_detail', post_pk=post_pk)


@login_required
def post_remove(request, post_pk):
	post = get_object_or_404(Post, pk=post_pk)
	post.delete()
	if post.published_date:
		return redirect('post_list')
	return redirect('post_draft_list')


def add_comment(request, post_pk):
	post = get_object_or_404(Post, pk=post_pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail', post_pk=post_pk)
	form = CommentForm()
	return render(request, 'blog/add_comment.html', {'post': post, 'form': form})


@login_required
def comment_approve(request, post_pk, comment_pk):
	comment = get_object_or_404(Comment, pk=comment_pk)
	comment.approve()
	return redirect('post_detail', post_pk=post_pk)


@login_required
def comment_remove(request, post_pk, comment_pk):
	comment = get_object_or_404(Comment, pk=comment_pk)
	comment.delete()
	return redirect('post_detail', post_pk=post_pk)
