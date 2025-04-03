from django.http import HttpResponse


def welcome(request):
    print("hello")
    return HttpResponse("Kese bhosdi walo")
