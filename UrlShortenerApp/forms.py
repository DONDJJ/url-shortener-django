from django import forms


class EnterUrlForm(forms.Form):
    user_original_url = forms.CharField(max_length=150)
