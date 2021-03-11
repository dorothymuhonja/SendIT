from flask import render_template, url_for
from . import main
from .forms import ParcelForm
from ..models import Parcel
from flask_login import login_required, current_user
from .. import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/parcel')
# @login_required
def parcel():
    form = ParcelForm()
    if form.validate_on_submit():
        details = form.details.data
        status = form.status.data
        location = form.location.data
        parcel = Parcel(details= details, status= status, location= location, sender= "current_user")
        
        db.session.add(parcel)
        db.session.commit()
        return render_template('parcel.html', form= form)



