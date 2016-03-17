from django.shortcuts import render
from django.http import HttpResponse
from trec_eval_app.forms import UserForm, UserProfileForm


#Creates html responses based the function called
#Each function contains a context_dict which contains variables to be used in the HTML template that is referenced

def index(request):
    context_dict = {'exampleDjangoVariable': "sdffgdgd!"}

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

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'trec_eval_app/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )