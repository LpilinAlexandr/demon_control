from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import DemonCheker
import subprocess

# один и тот же флажок на 2 функции
SUBJECT = 'checkbox'


def main(request):

    # Создаём или получаем флажок
    checkbox = DemonCheker.objects.get_or_create(subject=SUBJECT)[0]
    # Проверяем статус. Получем его в stdout
    check_sub = subprocess.run(["service", "apache2", "status"], stdout=subprocess.PIPE, text=True)
    status = check_sub.stdout
    service_name = check_sub.stdout[:8]

    context = {
        "checkbox": checkbox,
        "service_name": service_name,
        "status": status
    }

    # Проверяем запрос и выполняем соответствующую команду:
    if request.method == 'POST' and 'demon' in request.POST:
        if request.POST['demon'] == 'start':
            subprocess.run(["service", "apache2", 'start'], stdout=subprocess.PIPE, text=True)
        elif request.POST['demon'] == 'stop':
            subprocess.run(["service", "apache2", 'stop'], stdout=subprocess.PIPE, text=True)
        elif request.POST['demon'] == "restart":
            subprocess.run(["service", "apache2", "restart"], stdout=subprocess.PIPE, text=True)

        # Редиректим на главную
        return redirect(request.path)

    return render(request, 'demon/index.html', context)


def ajax_form(request):
    """
    Обрабатываем загруженные данные через ajax
    """

    # Проверяем запрос и вносим изменения в базу:
    if request.GET and 'checkbox' in request.GET:

        checkbox = DemonCheker.objects.get(subject=SUBJECT)

        if checkbox.state is True:
            # записываем в базу: "выключено"
            checkbox = DemonCheker.objects.get(subject=SUBJECT)
            checkbox.state = False
            checkbox.save()
            return HttpResponse(f"OFF")
        else:
            # записываем в базу: "включено"
            checkbox.state = True
            checkbox.save()
            return HttpResponse(f"ON")
    else:
        return