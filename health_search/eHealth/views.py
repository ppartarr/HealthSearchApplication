from django.shortcuts import render

from search.federated_search import federated_run_querys


def index(request):
    response = render(request, 'eHealth/index.html')
    return response


def about(request):
    return render(request, 'eHealth/about.html')


def search(request):
    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            result_list = federated_run_querys(query)
            print result_list

    return render(request, 'eHealth/search.html', {'result_list': result_list})
