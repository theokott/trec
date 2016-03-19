from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from trec_eval_app.forms import UserForm, UserProfileForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Creates html responses based the function called
# Each function contains a context_dict which contains variables to be used in the HTML template that is referenced


def index(request):
    context_dict = {'exampleDjangoVariable': "sdffgdgd!"}

    return render(request, 'trec_eval_app/index.html', context_dict)


def scoreboard(request):
    context_dict = {}

    return render(request, 'trec_eval_app/scoreboard.html', context_dict)


def user_login(request):
    context_dict = {}
    context_dict['login_error'] = None  # Reset login error message

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/trec_eval_app/')
            else:
                # These next two lines are for showing a red error message if user cant login in
                # Redirects them back to the login page with custom error message
                context_dict['login_error'] = 'Your TREC Eval account is disabled'
                return render(request, 'trec_eval_app/login.html', context_dict)
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)

            # These next two lines are for showing a red error message if user cant login in
            # Redirects them back to the login page with custom error message
            context_dict['login_error'] = 'Invalid login details supplied'
            return render(request, 'trec_eval_app/login.html', context_dict)
    else:
        return render(request, 'trec_eval_app/login.html', context_dict)


def register(request):

    context_dict = {}
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


def upload(request):
    context_dict = {}
    return render(request, 'trec_eval_app/upload.html', context_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/trec_eval_app/')


def user_profile(request):
    context_dict = {}
    return render(request, 'trec_eval_app/user.html', context_dict)