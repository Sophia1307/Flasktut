from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Sophia'}
	posts = [
		{
			'author': {'username': 'Pero'},
			'body': 'It is a sunny day here in Rijeka!'
		},
		{
			'author': {'username': 'Ivo'},
			'body': 'Za vikend je prognoza i dalje sunčano!'
		},
		{
			'author': {'username': 'Marica'},
			'body': 'Tko želi ići na izlet?'
		},
		{
			'author': {'username': 'Maro'},
			'body': 'Imam tri slobodna mjesta u autu!'
		}
		]
	return render_template('index.html', title='A blog', user=user, posts=posts)
