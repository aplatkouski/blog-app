from django import forms

from .models import Post, Comment, Choice


class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('title', 'text', 'is_pool')


class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('author', 'text')


class ChoiceForm(forms.ModelForm):

	class Meta:
		model = Choice
		fields = ('text', )
