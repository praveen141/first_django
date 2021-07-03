# Praveen created this file
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello Praveen</h1>")


def about(request):
    return HttpResponse("About Praveen")
