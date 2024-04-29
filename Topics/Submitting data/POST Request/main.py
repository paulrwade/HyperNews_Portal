
from django import forms
from django.shortcuts import redirect, Http404
from django.views import View


class TodoForm(forms.Form):

    todo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    important = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['todo'].widget.attrs.update({'class': 'form-control'})
        self.fields['important'].widget.attrs.update({'class': 'form-control'})


class TodoView(View):

    all_todos = []
    form_class = TodoForm
    template_name = 'form_template.html'

    def post(self, request, *args, **kwargs):

        todo = str(request.POST['todo']).strip()

        if todo not in self.all_todos:
            self.all_todos.append(todo)

        return redirect('/')
