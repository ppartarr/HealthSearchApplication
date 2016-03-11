import xml, json
import urllib, urllib2

if __name__ == '__main__':
    main()


def medlineplus_run_query(search_terms):
    root_url = "https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term="
    query = search_terms.replace(" ", "+")
    search_url = "{0}{1}".format(
        root_url,
        search_url
    )

    results=[]
    print search_url
    try:
        response = urllib2.urlopen(search_url).read()
        json_response = json.loads(response)

        for result in json_response['d']['results']:
            results.append({
                'title': result['Title'],
                'link': result['Url'],
                'summary': result['Description'],
                'from': 'Bing.com',
            })
    except urllib2.URLError as e:
        print "Error when querying the Medline+ API: ", e

    return results
