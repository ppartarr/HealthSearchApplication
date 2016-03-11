from django.shortcuts import render
from search.federated_search import federated_run_querys
from eHealth.forms import UserForm, UserProfileForm


def index(request):
    response = render(request, 'eHealth/index.html')
    return response


def about(request):
    return render(request, 'eHealth/about.html')


def search(request):
    result_list = {'federated_results': [],
                   'bing_results': [],
                   'healthFinder_results': [],
                   'medlinePlus_results': []
    }

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            result_list = federated_run_querys(query)
    return render(request, 'eHealth/search.html', result_list)


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

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'eHealth/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

