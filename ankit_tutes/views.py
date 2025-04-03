from django.http import HttpResponse


def welcome(request):
    print("hello")
    return HttpResponse("Responce from ankit")

def ishu(request):
    print("hello")
    return HttpResponse("Responce from ishu")
