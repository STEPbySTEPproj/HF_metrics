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
from wtforms.validators import DataRequired, NumberRange
# from urllib.parse import urlparse

class formLPP(FlaskForm):
    validated = False
    a = IntegerField('area a', [DataRequired(), NumberRange(min=0, max=10)], default=5)
    b = IntegerField('area b', [DataRequired(), NumberRange(min=0, max=10)], default=5)

    submit = SubmitField(label='Submit')