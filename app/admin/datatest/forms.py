from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields import (
    StringField,
    SubmitField,
)
from wtforms.validators import (
    Email,
    EqualTo,
    InputRequired,
    Length,
)

from app import db
from app.models import datatest

class DatatestForm(FlaskForm):

    name = StringField('Name', validators=[InputRequired(), Length(1, 64)])
    d1 = StringField('d1', validators=[InputRequired(), Length(1, 64)])
    d2 = StringField('d2', validators=[InputRequired(), Length(1, 64)])
    d3 = StringField('d3', validators=[InputRequired(), Length(1, 64)])
    d4 = StringField('d4', validators=[InputRequired(), Length(1, 64)])

    submit = SubmitField('Submit')