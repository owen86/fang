from flask import Flask
from flask import render_template
from flask import request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)
manager = Manager(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name = name)
	

@app.route('/getbrowser')
def getBrowser():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your brower is %s !</p>' % user_agent

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	render_template('500.html'),500

if __name__=='__main__':
	manager.run()