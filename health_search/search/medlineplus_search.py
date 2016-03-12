import xml.etree.ElementTree as ET
import urllib2
from django.utils.html import strip_tags

if __name__ == '__main__':
    main()


def medlineplus_run_query(search_terms):
    root_url = "https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term="
    query = search_terms.replace(" ", "+")
    search_url = "{0}{1}".format(
        root_url,
        query,
    )

    results = []
    try:
        response = urllib2.urlopen(search_url).read()
        # Convert the string response to a Python dictionary object
        xml_response = ET.fromstring(response)

        for document in xml_response.iter('document'):
            url = document.attrib.get('url')

            for content in document:
                if content.attrib.get('name') == 'title':
                    title = content.text
                if content.attrib.get('name') == 'snippet':
                    summary = content.text

            title = strip_tags(title)
            summary = strip_tags(summary)

            results.append({
                'link': url,
                'title': title,
                'summary': summary,
                'from': 'medline'})

    except urllib2.URLError as e:
        print "Error when querying the Medline+ API: ", e

    #print results
    return results


#medlineplus_run_query("asthma")
