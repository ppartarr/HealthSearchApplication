__author__ = 'Kevin'
import urllib2
from textstat.textstat import textstat
from textblob import TextBlob
from django.utils import html

######todo finish

#todo get url from db
url="http://www.tangowithdjango.com/book17/chapters/new17.html"

def _html_stripper(url):
    response = urllib2.urlopen(url)
    htmlresponce = response.read()
    #replaces <br> and <p> tags with newline charecter
    text=html.linebreaks(htmlresponce)
    #strips remaing html tags
    text=html.strip_tags(text)
    return text

def _get_readability_score(text):
    readability_score=textstat.flesch_reading_ease(text)
    return readability_score

def _get_polarity_score(text):
    polarity_score = TextBlob.polarity(text)
    #polarity is returns as a flot between (-1.0,1.0) this converts it to a int between (0,100)
    polarity_score = int(50+(polarity_score*50))
    return polarity_score


def _get_subjectivity_score(text):
    subjectivity_score = TextBlob.subjectivity(text)
    #subjectivity is returns as a flot between (0.0,1.0) this converts it to a int between (0,100)
    subjectivity_score = int(subjectivity_score*100)

    return subjectivity_score



def get_all_scores(url):
    try:
        text=_html_stripper(url)

        readability  = _get_readability_score(text)
        polarity     = _get_polarity_score(text)
        subjectivity = _get_subjectivity_score(text)

        return (readability,polarity,subjectivity)
    except:
        print 'error reading page'
        return(0,0,0)
#todo add score to db



