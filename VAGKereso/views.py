from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required as need_login
from .apps.tasks.models import ClassProfile

task_ids = {"A költő": 1,
            "Formalitás": 2,
            "Reliving": 3,
            "Keresési ág": 4,
            "Logikai ág": 5,
            "Művészeti ág": 6,
            "Irodalmi ág": 7,
            "Az utolsó játszma": 8,
            "A tekercs": 9}


def get_unlocked(class_profile: str) -> list:
    """Get the unlocked tasks."""

    tasks = class_profile.completed_tasks.all()
    print(set([task.name for task in tasks]))
    if all(task_name in [task.name for task in tasks] for
           task_name in ["Iker", "Szótenger", "A ritmus", "A tragédiák diktátora"]):
        value = True
    else:
        value = False

    tasks = [task.name for task in tasks if task.name in task_ids]
    print(tasks)
    if len(tasks) == 0:
        return [1]
    if task_ids.get(tasks[-1]) < 3:
        plus = 2
    elif value:
        plus = 6
    else:
        plus = 5

    print(list(range(1, task_ids.get(tasks[-1]) + plus)))
    return list(range(1, task_ids.get(tasks[-1]) + plus))


@need_login
def index(request: HttpRequest) -> HttpResponse:
    """Main Page"""

    unlocked = get_unlocked(request.user)

    return render(request, "index.html", {"buttons": unlocked})


@need_login
def logout(request: HttpRequest) -> HttpResponse:
    """Log Out and Redirect to the Login Page"""

    auth_logout(request=request)

    return redirect(to="login")


"""def register_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="create_user.html")


def register(request: HttpRequest) -> HttpResponse:
    classes = {"1A": "htuy8g",
               "1B": "tSvjxK",
               "1C": "WRmFvX",
               "2A": "srTsqA",
               "2B": "Bp081p",
               "2C": "omrCRO",
               "3A": "lvdAAj",
               "3B": "lp8MWc",
               "teachers": "fhpNUp",
               "tibor": "0jmlMD"}

    for username in classes:
        password = classes.get(username)

        ClassProfile.objects.create_user(username=username, password=password)

        print(f"{username} created.")

    return redirect("register")"""
