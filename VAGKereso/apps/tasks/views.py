from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required as need_login
from .models import Task, ClassProfile


def get_object(name: str) -> str:
    """Give the answer to the task."""

    for item in Task.objects.all():
        if item.name == name:
            return item


def normalize(string: str) -> str:
    """Normalize a string (eg.: convert á to a)"""

    original_letters = {"á": "a",
               "é": "e",
               "í": "i",
               "ó": "o",
               "ö": "o",
               "ő": "o",
               "ú": "u",
               "ü": "u",
               "ű": "u",
               " ": "_"}

    letters = {}

    for letter in original_letters:
        try:
            letters.update({letter: original_letters.get(letter),
                            letter.upper(): original_letters.get(letter).upper()})
        except:
            pass

    new_string = ""

    for character in string:
        if character in letters:
            new_string += letters.get(character)
            continue
        new_string += character

    return new_string


def get_unlocked(class_profile: ClassProfile, branch_name: str) -> list[int]:
    """Get the unlocked tasks in a branch."""

    # Get the completed tasks
    completed_tasks = [task.name for task in class_profile.completed_tasks.all()]

    # Define the branches
    branches = {"Keresés": {"Solar": 1,
                           "A kód": 2,
                           "Ősmagyarok dicsősége": 3,
                           "Iker": 4},
                "Logika": {"A játszma": 1,
                           "Iker 2": 2,
                           "Nézőpont": 3,
                           "Szótenger": 4},
                "Művészet": {"A piac": 1,
                             "A festmény": 2,
                             "A darab": 3,
                             "A ritmus": 4},
                "Irodalom": {"A mű": 1,
                             "A zseni": 2,
                             "Egy kutya": 3,
                             "A tragédiák diktátora": 4}}

    # Get the tasks in the current branch
    tasks_in_branch = branches.get(branch_name)

    # Get the completed tasks in the current branch
    completed_tasks = [tasks_in_branch.get(item) for item in completed_tasks if item in tasks_in_branch]

    if len(completed_tasks) == 0:
        return [1]
    return list(range(1, completed_tasks[-1] + 2))




@need_login
def task(request: HttpRequest, task_name: str) -> HttpResponse:
    """Show and test a task."""

    if request.method == "POST":
        answer = request.POST.get("answer")

        if answer:
            object = get_object(task_name)
            if answer.lower() == object.answer:
                request.user.add_task(object)
                return redirect("index")
    return render(request, normalize(task_name) + ".html")


@need_login
def branch_task(request: HttpRequest, task_name: str, branch_name: str) -> HttpResponse:
    if request.method == "POST":
        answer = request.POST.get("answer")

        if answer:
            object = get_object(task_name)
            if answer.lower() == object.answer:
                request.user.add_task(object)
                return redirect("tasks:" + normalize(branch_name).lower())
    return render(request, normalize(task_name) + ".html")

@need_login
def branch(request: HttpRequest, branch_name: str) -> HttpResponse:
    unlocked = get_unlocked(class_profile=request.user, branch_name=branch_name)
    return render(request, normalize(branch_name) + ".html", {"buttons": unlocked})


@need_login
def last_task(request: HttpRequest, task_name: str) -> HttpResponse:
    """Show and test the last task."""

    if request.method == "POST":
        answer = request.POST.get("answer")

        if answer:
            object = get_object(task_name)
            if answer.lower() == object.answer:
                request.user.add_task(object)
                return render(request=request, template_name="end.html")
    return render(request, normalize(task_name) + ".html")

