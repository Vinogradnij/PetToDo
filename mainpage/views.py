from django.shortcuts import render
from mainpage.models import Todo


# Create your views here.
menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Добавить', 'url_name': 'new_task'}]


def index(request):
    title = 'Задачи'
    tasks = Todo.objects.all()
    context = {
        'tasks': tasks,
        'title': title,
        'menu': menu
    }
    return render(request, 'mainpage/index.html', context=context)
