from django import forms


class CreateNewsItemForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))