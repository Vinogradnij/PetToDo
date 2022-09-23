from django.shortcuts import render
from mainpage.models import Todo


# Create your views here.

def index(request):
    title = 'Все задачи'
    tasks = Todo.objects.all()
    return render(request, 'mainpage/index.html', {'tasks': tasks, 'title': title})
