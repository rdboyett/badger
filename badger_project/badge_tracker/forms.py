from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=140,
        min_length=3,
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'search...',
                'required':'true'
            }))
