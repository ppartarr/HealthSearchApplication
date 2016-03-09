# todo check

import json
import urllib, urllib2
from keys import HealthFinder_key

HealthFinder_API_KEY = HealthFinder_key

if __name__ == '__main__':
    main()


def healthfinder_run_query(search_terms):
    root_url = 'http://healthfinder.gov/developer/'
    Return_Type = "json"

    query = "{0}".format(search_terms)
    query = urllib.quote(query)

    # todo dont hardcode
    gender = 'male'
    age = '30'

    search_url = "{0}Search.{1}?api_key={2}&gender={3}&age={4}&keyword={5}".format(
        root_url,
        Return_Type,
        HealthFinder_API_KEY,
        gender,
        age,
        query
    )

    print search_url
    results = []
    # healthfinder returns related items, these will be added to the end
    secondaryresults = []
    try:

        response = urllib2.urlopen(search_url).read()
        json_response = json.loads(response)

        if json_response['Result']['Error'] == 'False' and json_response['Result']['Total'] != '0':
            for result in json_response['Result']['Topics']:
                results.append({
                    'title': result['Title'],
                    'link': result['AccessibleVersion'],
                    'summary': result['Populations']})
                for secondaryresult in result['RelatedItems']:
                    print 'Title    test    ',secondaryresult['Title']
                    print 'Url      test    ',secondaryresult['Url']
                    print 'summary  test    ',result['Populations']
                    secondaryresults.append({
                        'title': secondaryresult['Title'],
                        'link': secondaryresult['Url'],
                        'summary': result['Populations']})


    except urllib2.URLError as e:
        print "Error when querying the HealthFinder API: ", e


    print 'primary'
    print
    print results
    print
    print 'secodary'
    print
    print secondaryresult

    results.append(secondaryresult)
    return results
