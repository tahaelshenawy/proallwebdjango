from django import forms


class loginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    taha= forms.CharField(max_length=50)

