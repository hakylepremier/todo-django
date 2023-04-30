from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from core.forms import AddTodoForm, EditTodoForm

from .models import Category, Todo

# Create your views here.
def index(request):
  todos = Todo.objects.all()
  categories = Category.objects.all()
  
  return render(request, 'core/index.html', {
    'categories': categories,
    'todos': todos,
  })
  
def toggleDone(request, id):
  todo = get_object_or_404(Todo, pk=id)
  todo.isChecked = not todo.isChecked
  todo.save()
  return HttpResponseRedirect(reverse('index'))

def add(request):
  todos = Todo.objects.all()
  categories = Category.objects.all()
  if request.method == 'POST':
    form = AddTodoForm(request.POST)
    if form.is_valid():
      todo = form.save(commit=False)
      todo.created_by = request.user
      todo.save()
      # process the data in form.cleaned_data as required
      # ...
      # redirect to a new URL:
      return HttpResponseRedirect(reverse('index'))
  else:
    form = AddTodoForm()
  return render(request, 'core/form.html', {
    'categories': categories,
    'todos': todos,
    "form": form,
  })
  
def edit(request, id):
    todos = Todo.objects.all()
    categories = Category.objects.all()
    todo = get_object_or_404(Todo, pk=id, created_by=request.user)

    if request.method == 'POST':
      form = EditTodoForm(request.POST, request.FILES, instance=todo)

      if form.is_valid():
        form.save()

      return HttpResponseRedirect(reverse('index'))
    else:
      form = EditTodoForm(instance=todo)

    return render(request, 'core/form.html', {
        'form': form,
        'categories': categories,
        'todos': todos,
    })
  
def delete(request, id):
  todo = get_object_or_404(Todo, pk=id, created_by=request.user)
  todo.delete()

  return HttpResponseRedirect(reverse('index'))