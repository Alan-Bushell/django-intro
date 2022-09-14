from django.shortcuts import render
from .models import Item


# Create your views here.
def get_todo_list(request):
    return render(request, 'todo/todo_list.html')
