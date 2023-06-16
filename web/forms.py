from django import forms


class MessageForm(forms.Form):
    text = forms.CharField(
        label = "Mensaje",
        max_length=200,
        widget=forms.Textarea(attrs={"class": "form-control", "rows":5}),
    )
    author = forms.CharField(
        label = "Autor",
        required = False,
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
