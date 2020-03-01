from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Comment, Choice
from .forms import PostForm, CommentForm, ChoiceForm


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
			if post.is_pool:
				return redirect('choice_edit', post_pk=post.pk)
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


@login_required
def choice_new(request, post_pk):
	post = get_object_or_404(Post, pk=post_pk)
	if request.method == "POST":
		form = ChoiceForm(request.POST)
		if form.is_valid():
			choice = form.save(commit=False)
			choice.pool = get_object_or_404(Post, pk=post_pk)
			choice.save()
	form = ChoiceForm()
	return render(request, 'blog/choice_new.html', {'post': post, 'form': form})


def choice_vote(request, post_pk):
	if request.method == "POST":
		try:
			choice_pk = request.POST['choice']
		except (KeyError, ):
			return redirect('post_detail', post_pk=post_pk)
		choice = get_object_or_404(Choice, pk=choice_pk)
		choice.vote()
	return redirect('post_detail', post_pk=post_pk)


@login_required
def choice_remove(request, post_pk, choice_pk):
	choice = get_object_or_404(Choice, pk=choice_pk)
	choice.delete()
	return redirect('post_edit', post_pk=post_pk)
