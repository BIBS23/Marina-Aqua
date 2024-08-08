from django.shortcuts import get_object_or_404, redirect,render
from .models import Todo

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    return render(request,'base/index.html',{'todos':todos})


def delete(request,pk):
    todo = get_object_or_404(Todo, pk=pk) 
    todo.delete()
    return redirect('home')


def addTodo(request):
    if request.method == 'POST':
        new_todo = Todo(title=request.POST['title'],descriptions=request.POST['description'])
        new_todo.save()
        return redirect('home')  # Redirect to the home view or appropriate URL
    
    return redirect('home')  # Redirect if the request method is not POST
