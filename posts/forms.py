from django import forms
from .models import Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=('user',)
        #fields='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content','rate']

    