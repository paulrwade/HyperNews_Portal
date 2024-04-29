
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

    all_todos = [['wash a dish', False], ['call mom', True], ['walk the dog', True], ['take a nap', False]]
    form_class = TodoForm
    template_name = 'form_template.html'

    def delete(self, request, todo, *args, **kwargs):

            todo = todo.strip()

            if todo in self.all_todos:
                self.all_todos.remove(todo)
            else:
                raise Http404('Todo item does not exist')

            return redirect('/')

