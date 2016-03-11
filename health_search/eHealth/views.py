from django.shortcuts import render
from search.federated_search import federated_run_querys


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


#todo implement
def user(request):
    response = render(request, 'eHealth/index.html')
    return response
