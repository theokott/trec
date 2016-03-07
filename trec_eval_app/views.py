from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'exampleDjangoVariable': "This is an example of a Django variable!"}

    return render(request, 'trec_eval_app/index.html', context_dict)
