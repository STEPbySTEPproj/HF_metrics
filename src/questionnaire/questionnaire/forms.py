from flask_wtf import FlaskForm
# from flask_wtf.file import FileRequired, FileAllowed, FileField

from wtforms import (
    IntegerField,
#     StringField,
     SubmitField,
#     SelectField,
#     SelectMultipleField,
#     PasswordField,
)
# from wtforms.widgets import ListWidget, CheckboxInput
# from wtforms.validators import Optional, DataRequired, InputRequired, Email, ValidationError
from wtforms.validators import DataRequired, InputRequired, NumberRange
# from urllib.parse import urlparse

class formLPP(FlaskForm):
    validated = False
    a = IntegerField('area a', [InputRequired(), NumberRange(min=0, max=10)])
    b = IntegerField('area b', [DataRequired(), NumberRange(min=0, max=10)])
    c = IntegerField('area c', [DataRequired(), NumberRange(min=0, max=10)])
    d = IntegerField('area d', [DataRequired(), NumberRange(min=0, max=10)])
    e = IntegerField('area e', [DataRequired(), NumberRange(min=0, max=10)])
    f = IntegerField('area f', [DataRequired(), NumberRange(min=0, max=10)])
    g = IntegerField('area g', [DataRequired(), NumberRange(min=0, max=10)])
    h = IntegerField('area h', [DataRequired(), NumberRange(min=0, max=10)])
    i = IntegerField('area i', [DataRequired(), NumberRange(min=0, max=10)])
    j = IntegerField('area j', [DataRequired(), NumberRange(min=0, max=10)])
    k = IntegerField('area k', [DataRequired(), NumberRange(min=0, max=10)])
    l = IntegerField('area l', [DataRequired(), NumberRange(min=0, max=10)])
    m = IntegerField('area m', [DataRequired(), NumberRange(min=0, max=10)])
    n = IntegerField('area n', [DataRequired(), NumberRange(min=0, max=10)])

    submit = SubmitField(label='Submit')