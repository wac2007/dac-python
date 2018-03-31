from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Seu nome', max_length=100)