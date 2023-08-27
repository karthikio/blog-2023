from django import forms
from .models import Post, Feedback


class postForm(forms.ModelForm):
  title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'title'}))
  # body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'body'}))
  
  class Meta:
    model = Post
    fields = ['title', 'info', 'body', 'image', 'tag', 'featured']
  

class FeedbackForm(forms.ModelForm):
  class Meta: 
    model = Feedback
    fields = ['name', 'content']