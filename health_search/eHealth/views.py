from django.shortcuts import render, HttpResponseRedirect,redirect
from search.federated_search import federated_run_querys
from eHealth.forms import UserForm, UserProfileForm, PageForm, CategoryForm
from eHealth.models import Category, Page, UserProfile
from django.contrib.auth import authenticate, login
from django.core.context_processors import request
from django.contrib.auth.models import User
from django.template import RequestContext


def default_context(request, dict):
    try:
        category_list = Category.objects.filter(public=True).order_by('-views')[:20]  # todo remove likes
        default = {'topcategories': category_list}
        default.update(dict)
        return default
    except:
        default = {}
        default.update(dict)
        return default


def index(request):
    response = render(request, 'eHealth/index.html', default_context(request, {}))
    return response


def about(request):
    return render(request, 'eHealth/about.html', default_context(request, {}))


def search(request):
    result_list = {'federated_results': [],
                   'bing_results': [],
                   'healthFinder_results': [],
                   'medlinePlus_results': [],
                   }

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            result_list = federated_run_querys(request, query)
    return render(request, 'eHealth/search.html', default_context(request, result_list))


# todo implement
def user(request):
    context_dict = {}
    try:
        user = UserProfile.objects.filter(user=request.user).get()
        context_dict['username'] = request.user.get_username()
        context_dict['email'] = request.user.email
        context_dict['dob'] = user.dateOfBirth
        context_dict['gender'] = user.gender
        context_dict['all_categories'] = Category.objects.filter(user=user)
    except:
        print 'user profile error:',
        return HttpResponseRedirect('/')
    response = render(request, 'eHealth/user.html', default_context(request, context_dict))
    return response


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

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
                  default_context(request, {'user_form': user_form, 'profile_form': profile_form, }))


def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        context_dict['category_name_slug'] = category.slug
        context_dict['category_views'] = category.views

        if request.POST:
            public = request.POST.get('public')
            category.public = (str(public)=='True')
            category.save()
        context_dict['public'] = category.public
        try:
            if str(request.user) == str(category.user):
                context_dict['is_owner'] = True
            else:
                context_dict['is_owner'] = False
        except:
            context_dict['is_owner'] = False

        #if you are not aurthrised to view a page you are returned to index
        if not (context_dict['is_owner'] or context_dict['public']):
            return HttpResponseRedirect('/')

    except Category.DoesNotExist:
        pass

    return render(request, 'eHealth/category.html', default_context(request, context_dict))


# todo fix need to add user to cat field
def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None
    print cat
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.get_scores()
                return HttpResponseRedirect('/category/'+category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat}

    return render(request, 'eHealth/add_page.html', default_context(request, context_dict))


def add_category(request):
    try:
        user = UserProfile.objects.get(user=request.user)
    except:
        user = None
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            if user:
                cat = form.save(commit=False)
                cat.user = user
                cat.save()
                return HttpResponseRedirect('/user')

        else:
            print form.errors
    else:
        form = CategoryForm()
    return render(request, 'eHealth/add_category.html', default_context(request, {'form': form}))


def track_url(request):
    page_id = None
    url = '/'
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = Page.objects.get(id=page_id)
                page.views = page.views + 1
                page.save()
                category = page.category
                category.views = category.views +1
                category.save()
                url = page.url
            except:
                pass

    return redirect(url)
