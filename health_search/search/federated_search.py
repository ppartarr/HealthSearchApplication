from bing_search import bing_run_query
from healthfinder_search import healthfinder_run_query
from medlineplus_search import medlineplus_run_query



def federated_run_querys(request,search_terms):
    Bing_results = bing_run_query(search_terms)
    HealthFinder_results = healthfinder_run_query(request,search_terms)
    MedlinePlus_results = medlineplus_run_query(search_terms)

    results = []

    # finds finds the shortest, mid and logest responce
    #put them into variables called longest, mid and shortest
    if len(Bing_results) >= len(HealthFinder_results) and len(Bing_results) >= len(MedlinePlus_results):
        longest = Bing_results
        if len(HealthFinder_results) >= len(MedlinePlus_results):
            mid = HealthFinder_results
            shortest = MedlinePlus_results
        else:
            mid = MedlinePlus_results
            shortest = HealthFinder_results
    elif len(HealthFinder_results) >= len(Bing_results) and len(HealthFinder_results) >= len(MedlinePlus_results):
        longest = HealthFinder_results
        if len(Bing_results) >= len(MedlinePlus_results):
            mid = Bing_results
            shortest = MedlinePlus_results
        else:
            mid = MedlinePlus_results
            shortest = Bing_results
    else:
        longest = MedlinePlus_results
        if len(HealthFinder_results) >= len(Bing_results):
            mid = HealthFinder_results
            shortest = Bing_results
        else:
            mid = Bing_results
            shortest = HealthFinder_results

    #combines results from the api's into one list
    #mergis the results untill a list runs out, then merges the remain lists
    for i in range(len(shortest)):
        results.append(longest[i])
        results.append(mid[i])
        results.append(shortest[i])

    for i in range(len(shortest), len(mid)):
        results.append(longest[i])
        results.append(mid[i])

    for i in range(len(mid), len(longest)):
        results.append(longest[i])

    return {'federated_results': results,
            'bing_results': Bing_results,
            'healthFinder_results': HealthFinder_results,
            'medlinePlus_results': MedlinePlus_results
    }
