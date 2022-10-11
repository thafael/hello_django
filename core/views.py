from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1 style="color:green; text-align: center; text-shadow:  2px 2px purple;"> Hello World {} tem {} de idade</h1>'.format(nome, idade))

