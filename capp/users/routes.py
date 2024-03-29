from flask import render_template, Blueprint, redirect, flash, url_for
from capp.users.forms import RegistrationForm, LoginForm

users=Blueprint('users',__name__)

@users.route('/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash('Your account has been created! Now, your are able to login!','Sucess')
    return redirect (url_for('home.home_home'))
  return render_template('users/register.html', title='register', form= form)

@users.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('You Have Logged In! Now you are able to use the Carbon App!', 'Sucess')
    return redirect (url_for('home.home_home'))
  return render_template('users/login.html', title='login', form= form)
