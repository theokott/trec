from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from trec_eval_app.forms import UserForm, UserProfileForm, RunUploadForm
from django.contrib.auth.decorators import login_required
from trec_eval_app.models import Track, Run

# Creates html responses based the function called
# Each function contains a context_dict which contains variables to be used in the HTML template that is referenced


def index(request):
    context_dict = {'request': request}

    return render(request, 'trec_eval_app/index.html', context_dict)


def scoreboard(request, track_slug=-1):
    context_dict = {'request': request}

    all_tracks = Track.objects.all()
    this_track = []

    if track_slug == -1:
        runs = Run.objects.all()
    else:
        for track in all_tracks:
            if track.slug == track_slug:
                this_track = track
                break

        runs = Run.objects.filter(track=this_track)

    context_dict['tracks'] = all_tracks
    context_dict['this_track'] = this_track
    context_dict['runs'] = runs

    return render(request, 'trec_eval_app/scoreboard.html', context_dict)


def user_login(request):
    context_dict = {'request': request}
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

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        context_dict['user_form'] = user_form
        context_dict['profile_form'] = profile_form

    context_dict['registered'] = registered
    context_dict['request'] = request

    return render(request, 'trec_eval_app/register.html', context_dict)


def upload(request):
    context_dict = {'request': request}

    if request.method == 'POST':
        upload_form = RunUploadForm(data=request.POST)

        if upload_form.is_valid():
            run = upload_form.save(commit=False)

            if 'file' in request.FILES:
                run.file = request.FILES['file']

            run.save()

        else:
            print upload_form.errors

    else:
        upload_form = RunUploadForm()
        context_dict['upload_form'] = upload_form

    context_dict['request'] = request

    return render(request, 'trec_eval_app/upload.html', context_dict)


    return render(request, 'trec_eval_app/upload.html', context_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/trec_eval_app/')


def user_profile(request):
    context_dict = {'request': request}
    user = request.user
    profile = user.userprofile
    context_dict['university'] = profile.university
    context_dict['description'] = profile.description
    context_dict['picture'] = profile.picture
    return render(request, 'trec_eval_app/user.html', context_dict)


@login_required
def user_edit_profile(request):
    context_dict = {'request': request}
    context_dict['error_message'] = None
    user = request.user
    profile = user.userprofile

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=profile)

        if all([user_form.is_valid(), profile_form.is_valid()]):
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('trec_eval_app/user.html')
    else:
        context_dict['university'] = profile.university
        context_dict['description'] = profile.description
        context_dict['picture'] = profile.picture

    return render(request, 'trec_eval_app/edit-profile.html', context_dict)


def user_edit_password(request):
    context_dict = {'request': request}
    context_dict['error_message'] = None
    user = request.user
    profile = user.userprofile

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=profile)

        if all([user_form.is_valid(), profile_form.is_valid()]):
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('trec_eval_app/user.html')
    else:
        context_dict['university'] = profile.university
        context_dict['description'] = profile.description
        context_dict['picture'] = profile.picture
    return render(request, 'trec_eval_app/edit-password.html', context_dict)
