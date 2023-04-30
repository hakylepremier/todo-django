from django import forms

from .models import Category, Todo

# class AddTodoForm(forms.Form):
#   categories = Category.objects.all().values()
#   print(categories)
#   # categories_list = list(categories)
  
#   title = forms.CharField(label='Your name', max_length=100)
#   description = forms.CharField(widget=forms.Textarea)
#   category = forms.ChoiceField(
#         widget=forms.RadioSelect(attrs={
#           'class': "yes"
#         }),
#         choices=categories,
         
#     )
CLASSES = 'todo-form-category'

class AddTodoForm(forms.ModelForm):
  
  class Meta:
    categories = Category.objects.all().values()
    model = Todo
    fields = ('name', 'description', 'category',)
    widgets = {
      'name': forms.TextInput(attrs={
          'class': 'todo-input-title todo-input',
          'placeholder': 'Add a title',
      }),
      'description': forms.Textarea(attrs={
          'class': 'todo-input-descr todo-input',
          'placeholder': 'Add a description',
      }),
      'category': forms.RadioSelect(attrs={
          'class': CLASSES
      },choices=categories)
    }
    
class EditTodoForm(forms.ModelForm):
  
  class Meta:
    categories = Category.objects.all().values()
    model = Todo
    fields = ('name', 'description', 'category',)
    widgets = {
      'name': forms.TextInput(attrs={
          'class': 'todo-input-title todo-input',
          'placeholder': 'Add a title',
      }),
      'description': forms.Textarea(attrs={
          'class': 'todo-input-descr todo-input',
          'placeholder': 'Add a description',
      }),
      'category': forms.RadioSelect(attrs={
          'class': CLASSES
      },choices=categories)
    }
    