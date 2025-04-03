
from django.http import HttpResponse

def welcome(request):
    print("hello")
    return HttpResponse("Hello welcome to ankit project")
