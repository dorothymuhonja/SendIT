from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
import email_validator
from wtforms.validators import Required 

class ParcelForm(FlaskForm):
    details = db.Column(db.TextAreaField(140))
    status = StringField('Status', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Add Parcel')