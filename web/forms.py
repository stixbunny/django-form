from django import forms


class MessageForm(forms.Form):
    text = forms.CharField(
        max_length=200,
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )
    author = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
