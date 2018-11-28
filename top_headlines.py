from flask import Flask, render_template
from datetime import datetime
import secrets
import requests

nyt_key = secrets.api_key

app = Flask(__name__)

time = str(datetime.now()).split()
time = time[1].split(':')
hour = time[0]
hour = int(hour)

greeting = ''
if(hour < 13):
	greeting = 'Good morning'
elif(hour > 12 and hour < 17):
	greeting = 'Good afternoon'
elif(hour > 16 and hour < 21):
	greeting = 'Good evening'
else:
	greeting = 'Good night'

def get_stories(section):
	baseurl ='https://api.nytimes.com/svc/topstories/v2/' 
	extendedurl = baseurl + section +'.json' 
	params={'api-key': nyt_key}
	return requests.get(extendedurl, params).json()

section ='technology'
stories = get_stories(section)
headlines = []

for i in range(len(stories['results'])):
	if(stories['results'][i]['section'] == 'Technology'):
		article = stories['results'][i]['title']
		link = stories['results'][i]['short_url']
		headlines.append(str(article) + ' (' + str(link) + ')')

top5 = headlines[:5]

@app.route('/')
def index():    
    return '<h1>Welcome!</h1>'

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',GREET = greeting ,NAME = name, article_list = top5)
	pass

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)