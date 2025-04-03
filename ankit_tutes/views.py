
from django.http import HttpResponse

def welcome(request):
    print("hello")
    return HttpResponse("Hello welcome to anshu project")

def ishu(request):
    print("Jagdish ki maka bhosda")
    return HttpResponse("puppu ki maka bhosda")