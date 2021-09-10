from django import forms


class NewWikiForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(widget=forms.Textarea)
