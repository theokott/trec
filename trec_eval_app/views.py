from django.shortcuts import render
from django.http import HttpResponse


#Creates html responses based the function called
#Each function contains a context_dict which contains variables to be used in the HTML template that is referenced

def index(request):
    context_dict = {'exampleDjangoVariable': "This is an example of a Django variable!"}

    return render(request, 'trec_eval_app/index.html', context_dict)

def scoreboard(request):
    context_dict = {}

    return render(request, 'trec_eval_app/scoreboard.html', context_dict)

def login(request):
    context_dict = {}
    return render(request, 'trec_eval_app/login.html', context_dict)

def register(request):
        context_dict = {}
        return render(request, 'trec_eval_app/register.html', context_dict)