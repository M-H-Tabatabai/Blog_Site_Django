from django import forms
from captcha.fields import CaptchaField
from website.models import Contact, Newsletter

class ContactFormSimple(forms.Form):
    captcha = CaptchaField()
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea())
    
class ContactModelForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = "__all__"

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

class NewsletterForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Newsletter
        fields = "__all__"