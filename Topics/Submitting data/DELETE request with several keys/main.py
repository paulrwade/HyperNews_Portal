from django import forms
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

    all_todos = [['wash a dish', False], ['call mom', True], ['walk the dog', True], ['take a nap', False]]
    form_class = TodoForm
    template_name = 'form_template.html'

    def delete(self, request, todo, important, *args, **kwargs):

        # form = self.form_class(request.POST)
        #
        # if form.is_valid():

            # todo = bool(form.cleaned_data['todo'])
            # important = bool(form.cleaned_data['important'])

            # if not important:
            #     for todo_item in self.all_todos:
            #         if todo_item['todo'] == todo:
            #             self.all_todos.remove(todo_item)

        for todo_item in self.all_todos:
            if not bool(todo_item[1]):
                self.all_todos.remove(todo_item)

        return redirect('/')
