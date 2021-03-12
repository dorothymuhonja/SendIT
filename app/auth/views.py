from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from . import auth
from werkzeug.security import generate_password_hash

@auth.route('/register',methods= ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data,password_hash=generate_password_hash(form.password.data))

        db.session.add(user)
        db.session.commit()


        flash('Account created successfully', 'success')

        return redirect(url_for('auth.login'))
        title = 'New Account'
        form = RegistrationForm()
    return render_template('auth/register.html',form=form)

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.parcel'))

        flash('Invalid email or password')

    title = 'SendIT login'
    return render_template('auth/login.html', form=form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))