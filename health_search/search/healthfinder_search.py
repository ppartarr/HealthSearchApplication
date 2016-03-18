# todo check

import json
import urllib, urllib2
from keys import HealthFinder_key
from eHealth.models import UserProfile
import datetime



HealthFinder_API_KEY = HealthFinder_key


def healthfinder_run_query(request,search_terms):
    primary_results = []
    # healthfinder returns related items, these will be added to the end
    secodary_results = []
    root_url = 'http://healthfinder.gov/developer/'
    Return_Type = "json"

    query = "{0}".format(search_terms)
    query = urllib.quote(query)

    #healthfinder requers age and gender
    #if user is not loged in default age and gender are used
    gender = 'female'
    age = '35'

    #if they are there age and gender are used
    if request.user.is_authenticated():
        user = UserProfile.objects.filter(user=request.user).get()
        gender = user.gender
        age =  str(datetime.date.today().year-user.dateOfBirth.year)


    search_url = "{0}Search.{1}?api_key={2}&gender={3}&age={4}&keyword={5}".format(
        root_url,
        Return_Type,
        HealthFinder_API_KEY,
        gender,
        age,
        query
    )
    try:
        keys=[]
        response = urllib2.urlopen(search_url).read()
        json_response = json.loads(response)

        if json_response['Result']['Error'] == 'False' and json_response['Result']['Total'] != '0':
            #does not run is there are no responcese
            #if there is one responce json_response['Result']['Topics'] is a dict else it is a list of dicts
            dict={}
            if json_response['Result'].has_key('Topics'):
                keys+=['Topics']
            if json_response['Result'].has_key('Tools'):
                keys+=['Tools']
            for key in keys:
                if json_response['Result']['Total'] == '1':
                    _extract_info(json_response['Result'][key],primary_results,secodary_results)
                else:
                    for result in json_response['Result'][key]:
                        _extract_info(result,primary_results,secodary_results)

    except urllib2.URLError as e:
        print "Error when querying the HealthFinder API: ", e

    results = primary_results + secodary_results

    return results


def _extract_info(result,primary_results,secodary_results):
    try:
        primary_results.append({
            'title': result['Title'],
            'link': result['AccessibleVersion'],
            'summary': result['Populations'],
            'from': 'HealthFinder.gov'})
    except:
        print 'Error extracting healthfinder primary_results'
    try:
        for secodary_result in result['RelatedItems']:
            secodary_results.append({
                'title': secodary_result['Title'],
                'link': secodary_result['Url'],
                'summary': result['Populations'],
                'from': 'HealthFinder.gov'})
    except:
        print 'Error extracting healthfinder secodary_results'