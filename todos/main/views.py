from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from main.models import Todo
from main.forms import TodoForm
from django.contrib import messages
from django.views.generic import CreateView,UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class HomePageListView(ListView):
    queryset = Todo.objects.all()
    template_name = 'main/home.html'
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['today'] = datetime.now()
        ctx['app_name'] = 'Wobble Todos'
        return ctx



def homePageView(request):
    todos = Todo.objects.all()
    context = {'today':datetime.now(), 'app_name':'Wobble Todos','todos':todos}

    return render(request, 'main/home.html',context)

def contactPageView(request):
    return render(request, 'main/contact.html')

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'main/detail.html'

def todo_detailPageView(request, todo_id):
    todo = get_object_or_404(Todo,pk=todo_id)
    context = {'todo':todo }
    return render(request,'main/detail.html',context)

class TodoCreateView(SuccessMessageMixin,CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'main/todo.html'
    success_url = reverse_lazy('home')
    success_message = 'Todo created successfully!'


def todo_createPageView(request):
    if request.method == 'POST':
        todo = TodoForm(request.POST)
        if todo.is_valid():
            todo.save()
            messages.success(request, 'the todo messages was created successfully')
            return redirect('home')
        return render(request, 'main/todo.html', {"form":todo})
    return render(request, 'main/todo.html', {'form':TodoForm()})

class TodoUpdateView(SuccessMessageMixin,UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'main/todo.html'
    success_url = reverse_lazy('home')
    success_message = 'Todo updated successfully!'




def todo_updatePageView(request, todo_id):
    todo = get_object_or_404(Todo,pk=todo_id)
    if request.method == 'POST':
        todo = TodoForm(request.POST, instance=todo)
        if todo.is_valid():
            todo.save()
            messages.success(request, 'the todo messages was updated successfully')
            return redirect('home')
        return render(request, 'main/todo.html', {"form":todo})
    return render(request, 'main/todo.html', {'form':TodoForm(instance=todo)})
