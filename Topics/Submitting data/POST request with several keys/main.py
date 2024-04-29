from django import forms
from django.forms import ModelForm
from django.shortcuts import redirect
from django.views import View


class TodoForm(forms.Form):

    todo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    important = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['todo'].widget.attrs.update({'class': 'form-control'})
        self.fields['important'].widget.attrs.update({'class': 'form-control'})


class TodoView(View):

    form_class = TodoForm
    all_todos = ['wash a dish']
    template_name = 'form_template.html'

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():

            todo = form.cleaned_data['todo']
            important = form.cleaned_data['important']

            for todo_item in self.all_todos:
                if todo_item == todo:
                    self.all_todos.remove(todo_item)

            if important:
                self.all_todos.insert(0, todo)
            else:
                self.all_todos.append(todo)

        return redirect('/')
