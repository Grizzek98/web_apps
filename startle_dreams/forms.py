from django import forms

class PostForm(forms.Form):
    title = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Date"
            }
        )
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter body here"
            }
        )
    )