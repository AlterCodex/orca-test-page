from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput


class WorkingContactForm(forms.Form):
    template_name = "apply-form.html"

    user_name = forms.CharField(label="Name")
    mail = forms.CharField(label="Your Email")
    web_page = forms.URLField(label="Linkedin")
    captcha = CaptchaField(label="Are you a Human")
