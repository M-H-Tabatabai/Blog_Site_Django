from django import forms
from captcha.fields import CaptchaField
from blog.models import Comment

class CommentForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'subject', 'message']