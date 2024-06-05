from django.shortcuts import render


def index(request):
    print(request.user)
    return render(request, "base.html", {"id": "1C"})
