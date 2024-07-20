from django.shortcuts import render, redirect
from .models import ToDo
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


def index(request):
    data = {
        'title': 'Home page',
        'todo_list': ToDo.objects.all()
	}
    return render(request, 'todoapp/index.html', data)


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    # Тайтл применяет request из формы 'title' это название нашей формы
    todo = ToDo(title=title)
    # Обращаемся к ToDo и для тайтл записываем тайтл 
    todo.save()
    # Сохраняем тайтл в базу данных
    return redirect('index')
	# И после создания мы возвращаемся на index функцию  


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    # Тут мы будем искать нашу todo, искать мы ее будем по id.
    # В Django мы сначала обращаемся к модели потом к объектам модели.
    # С помощью метода get мы ищем по id наш todo_id
    todo.is_complete = not todo.is_complete
    # Так же для todo которую мы создали выше поле is_complete мы ставим not 
    todo.save()
    # Сохраняем изменения в базе данных.
    return redirect('index')
    # Возвращаемся на index функцию

def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    # Тоже самое что и в функции выше, мы сначала ищем todo по id
    todo.delete()
    # Удаляем todo
    return redirect('index')
	# Возвращаемся на index функцию