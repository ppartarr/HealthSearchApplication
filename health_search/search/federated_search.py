from bing_search import bing_run_query
from healthfinder_search import healthfinder_run_query
from medlineplus_search import medlineplus_run_query



if __name__ == '__main__':
    main()

#todo finish
def run_querys(search_terms):
    Bing_results= bing_run_query(search_terms)
    HealthFinder_results= healthfinder_run_query(search_terms)
    MedlinePlus_results= medlineplus_run_query(search_terms)

    results =[]

    longest=max(len(Bing_results),len(HealthFinder_results),len(MedlinePlus_results))

    for i in range(longest):
        foo='bar'


    return results