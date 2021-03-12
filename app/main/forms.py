from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
import email_validator
from wtforms.validators import Required 

class ParcelForm(FlaskForm):
    details =TextAreaField('Enter parcel details', validators=[Required()])
    status = StringField('Status', validators=[Required()])
    location = StringField('Location', validators=[Required()])
    recipient = StringField('Recipient', validators=[Required()])
    submit = SubmitField('Add Parcel')