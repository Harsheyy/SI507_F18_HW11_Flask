from flask import Flask
from datetime import datetime
import secrets
import requests

api_key = secrets.api_key

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

@app.route('/')
def index():    
    return '<h1>Welcome!</h1>'

@app.route('/user/<name>')
def user(name):
	return '<h1>%s, %s!</h1>' % (greeting, name)

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)