from django.shortcuts import render, HttpResponseRedirect
from search.federated_search import federated_run_querys
from eHealth.forms import UserForm, UserProfileForm, PageForm, CategoryForm
from eHealth.models import Category,Page,UserProfile
from django.contrib.auth import authenticate, login
from django.core.context_processors import request
from django.template import RequestContext


def default_context(dict):
    try:
        user = request.user.get_username()
        category_list = Category.objects.filter(user=user).order_by('-likes')[:5]
        page_list = Page.objects.filter(user=user).order_by('-views')[:5]
        default= {'categories': category_list, 'pages': page_list}
        default.update(dict)
        return default
    except:
        default={}
        default.update(dict)
        return default

def index(request):
    response = render(request, 'eHealth/index.html',default_context({}))
    return response


def about(request):
    return render(request, 'eHealth/about.html',default_context({}))


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
    return render(request, 'eHealth/search.html', default_context(result_list))


#todo implement
def user(request):

    user=UserProfile.objects.filter(user=request.user).get()
    context_dict = {}
    context_dict['username']        = request.user.get_username()
    context_dict['email']           = request.user.email
    context_dict['dob']             = user.dateOfBirth
    context_dict['gender']          = user.gender
    context_dict['all_caegories']   = Category.objects.filter(user=user)
    response = render(request, 'eHealth/user.html',default_context(context_dict))
    return response



def register(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

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
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password'],
                                    )
            login(request, new_user)

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'registration/register.html',
            default_context({'user_form': user_form, 'profile_form': profile_form, 'registered': registered}))

def category(request, category_name_slug):
    context_dict = {}

    try:

        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        context_dict['category_name_slug'] = category.slug

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, 'eHealth/category.html', context_dict)


#todo fix need to add user to cat field
def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat}

    return render(request, 'eHealth/add_page.html', context_dict)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()
    return render(request, 'eHealth/add_category.html', {'form': form})