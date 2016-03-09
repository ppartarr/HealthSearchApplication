# todo check

import json
import urllib, urllib2
from keys import HealthFinder_key

HealthFinder_API_KEY = HealthFinder_key

if __name__ == '__main__':
    main()


def run_query(search_terms):
    root_url = 'http://healthfinder.gov/developer/'
    Return_Type = "Json"

    query = "'{0}'".format(search_terms)
    query = urllib.quote(query)

    search_url = "{0}Search.{1}?api_key={2}&keyword={3}".format(
        root_url,
        Return_Type,
        HealthFinder_API_KEY,
        query
    )

    results = []

    try:

        response = urllib2.urlopen(search_url).read()

        json_response = json.loads(response)

        if json_response['Result']['Error'] == 'False'
            for result in json_response['Result']['Topics']
                results.append({
                    'title': result['Title'],
                    'link': result['AccessibleVersion'],
                    'summary': result['MyHFDescription']})
    except urllib2.URLError as e:
        print "Error when querying the HealthFinder API: ", e

    return results