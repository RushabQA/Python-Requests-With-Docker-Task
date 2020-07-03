from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class AnimalForm(FlaskForm):
    animal = Stringfield('animal')
    noise = Stringfield('noise')

    submit = SubmitField('submit')
