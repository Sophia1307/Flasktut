from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sophia'}
    posts = [
        {
            'author': {'username': 'Peter'},
            'body': 'It is a sunny day here in Rijeka!'
        },
        {
            'author': {'username': 'John'},
            'body': 'Will be sunny on weekend!'
        },
        {
            'author': {'username': 'Mary'},
            'body': 'Who wants to go for a walk?'
        },
        {
            'author': {'username': 'Paul'},
            'body': 'I am in!'
        }
    ]
    return render_template(
        'index.html',
        title='A blog',
        user=user,
        posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
