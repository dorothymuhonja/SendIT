from flask import render_template, url_for, request, flash, redirect
from . import main
from .forms import ParcelForm
from ..models import Parcel, User
from flask_login import login_required, current_user
from .. import db


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/parcel', methods=['GET', 'POST'])
@login_required
def parcel():
    form = ParcelForm()
    if form.validate_on_submit():
        details = form.details.data
        status = form.status.data
        location = form.location.data
        recipient = form.recipient.data
        parcel = Parcel(details= details, status= status, location= location, sender= current_user)
        
        db.session.add(parcel)
        db.session.commit()


    return render_template('parcel.html', form=form)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    user_id = current_user.id
    parcels = Parcel.query.filter_by(user_id=user_id).all()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user=user, parcels=parcels)

@main.route('/parcels/<int:parcel_id>/delete', methods = ['POST', 'GET'])
@login_required
def delete(parcel_id):
    parcel = Parcel.query.get(parcel_id)
    if parcel.sender != current_user:
        abort(403)
    
    
    db.session.delete(parcel)
    db.session.commit()
    
    return redirect(url_for('.index',parcel=parcel))

@main.route('/parcel/<parcel_id>/update', methods = ['GET','POST'])
@login_required
def update_parcel(parcel_id):
    parcel = Parcel.query.get(parcel_id)
    if parcel.sender != current_user:
        abort(403)
        
    form = ParcelForm()
    if form.validate_on_submit():
        parcel.details = form.details.data
        parcel.status = form.status.data
        parcel.location = form.location.data
        parcel.recipient = form.recipient.data
       
        db.session.commit()
        
        flash('You have updated your Parcel!', 'success')
        
        return redirect(url_for('main.index',id = parcel.id)) 
    
    if request.method == 'GET':
        form.details.data = parcel.details 
        form.status.data = parcel.status 
        form.location.data = parcel.location 
        form.recipient.data = parcel.recipient 
        
        
    return render_template('parcel.html', form = form, legend='Update Parcel')

@main.route('/admin')
@login_required
def admin():
    parcels = Parcel.query.all()

    return render_template('admin.html', parcels=parcels)