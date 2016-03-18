__author__ = 'Kevin'
import urllib2
from textstat.textstat import textstat
from textblob import TextBlob
from django.utils import html



def _html_stripper(url):
    response = urllib2.urlopen(url)
    htmlresponce = response.read()
    # replaces <br> and <p> tags with newline charecter
    text = html.linebreaks(htmlresponce)
    # strips remaing html tags
    text = html.strip_tags(text)
    return text


def _get_readability_score(text):
    try:
        readability_score = textstat.flesch_reading_ease(text)
        return readability_score
    except:
        print '_get_readability_score'
        return 0


def _get_polarity_score(text):
    try:
        polarity_score = TextBlob(text).polarity
        # polarity is returns as a flot between (-1.0,1.0) this converts it to a int between (0,100)
        polarity_score = int(50 + (polarity_score * 50))
        return polarity_score
    except:
        print '_get_polarity_score Error'
        return 0


def _get_subjectivity_score(text):
    try:
        subjectivity_score = TextBlob(text).subjectivity
        # subjectivity is returns as a flot between (0.0,1.0) this converts it to a int between (0,100)
        subjectivity_score = int(subjectivity_score * 100)

        return subjectivity_score
    except:
        print '_get_subjectivity_score Error'
        return 0


def get_all_scores(url):
    try:
        text = _html_stripper(url)
    except:
        print 'error reading page'
        return (0, 0, 0)  # todo add score to db

    readability = _get_readability_score(text)
    polarity = _get_polarity_score(text)
    subjectivity = _get_subjectivity_score(text)

    return (readability, polarity, subjectivity)

