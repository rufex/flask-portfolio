from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Enter your name.")])
    email = StringField('Mail', validators=[DataRequired(message="Enter your email."), Email(message="Enter a valid email.")])
    subject = StringField('Subject', validators=[DataRequired(message="Enter your subject.")])
    message = StringField('Message', widget=TextArea(), validators=[DataRequired(message="Enter your message.")])
    send = SubmitField('Send')
    # add recaptcha