from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Sydney'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Smoky day in Portland!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'Raised by Wolves is okay'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

