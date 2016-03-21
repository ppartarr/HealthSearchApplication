## Search App
###Team Members 
* thekevinchi         : Kevin       2079830
* JDHL                : Duy Hieu    2140233 
* 2142915, gallicism  : Philippe    2142915
* aratherstrangeman   : Christopher 2128878

### Installation Guide (python 2.7 requiered):
1. Clone the repo               : git clone https://github.com/thekevinchi/HSA.git
2. Create a virtual enviroment  : mkvirtualenv eHealth
3. Enable virtual enviroment    : workon eHealth
4. Change directory             : cd HSA
5. Install python requirements  : pip install -r requirements.txt
6. Change directory             : cd health_search
7. Create the database          : python manage.py syncdb
8. Populate the database        : python populate_db.py
*  To run localhost             : python manage.py runserver 