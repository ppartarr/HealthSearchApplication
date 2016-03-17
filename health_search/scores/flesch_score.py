__author__ = 'Kevin'
import urllib2
from textstat.textstat import textstat

######todo finish

#todo get url from db
url="https://en.wikipedia.org/wiki/Python_(programming_language)"

def get_flesch_reading_ease_score(url):
    url="https://en.wikipedia.org/wiki/Python_(programming_language)"
    response = urllib2.urlopen(url)
    html = response.read()
    htmlscore=textstat.flesch_reading_ease(html)
    print htmlscore
    print html


    print '\n\n\n'
    text=html2text.html2text(html)
    print type(text)
    #testscore=textstat.flesch_reading_ease(text)
    #print testscore

get_flesch_reading_ease_score(url)

#todo add score to db