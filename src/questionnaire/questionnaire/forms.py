from flask_wtf import FlaskForm
# from flask_wtf.file import FileRequired, FileAllowed, FileField

from wtforms import (
    IntegerField,
#     StringField,
    SubmitField,
    RadioField,
#     SelectField,
#     SelectMultipleField,
#     PasswordField,
)
# from wtforms.widgets import ListWidget, CheckboxInput
# from wtforms.validators import Optional, DataRequired, InputRequired, Email, ValidationError
from wtforms.validators import InputRequired, NumberRange
# from urllib.parse import urlparse

class formLPP(FlaskForm):
    validated = False
    a = IntegerField('area a', [InputRequired(), NumberRange(min=0, max=10)])
    b = IntegerField('area b', [InputRequired(), NumberRange(min=0, max=10)])
    c = IntegerField('area c', [InputRequired(), NumberRange(min=0, max=10)])
    d = IntegerField('area d', [InputRequired(), NumberRange(min=0, max=10)])
    e = IntegerField('area e', [InputRequired(), NumberRange(min=0, max=10)])
    f = IntegerField('area f', [InputRequired(), NumberRange(min=0, max=10)])
    g = IntegerField('area g', [InputRequired(), NumberRange(min=0, max=10)])
    h = IntegerField('area h', [InputRequired(), NumberRange(min=0, max=10)])
    i = IntegerField('area i', [InputRequired(), NumberRange(min=0, max=10)])
    j = IntegerField('area j', [InputRequired(), NumberRange(min=0, max=10)])
    k = IntegerField('area k', [InputRequired(), NumberRange(min=0, max=10)])
    l = IntegerField('area l', [InputRequired(), NumberRange(min=0, max=10)])
    m = IntegerField('area m', [InputRequired(), NumberRange(min=0, max=10)])
    n = IntegerField('area n', [InputRequired(), NumberRange(min=0, max=10)])

    submit = SubmitField(label='Submit')

class formUEI(FlaskForm):
    validated = False
    a = RadioField('Time required to donning the exoskeleton', validators=[InputRequired()], choices=[('c1', '0-1min'),('c2', '5-10min'),('c3', '>10min')])
    b = RadioField('Time required to doffing the exoskeleton', validators=[InputRequired()], choices=[('c1', '0-1min'),('c2', '5-10min'),('c3', '>10min')])
    c = RadioField('Number of stair levels climbed up', validators=[InputRequired()], choices=[('c1', '4-6'),('c2', '2-4'),('c3', '0-1')])
    d = RadioField('Number of stair levels climbed down', validators=[InputRequired()], choices=[('c1', '4-6'),('c2', '2-4'),('c3', '0-1')])
    e = RadioField('Number of steps walked up', validators=[InputRequired()], choices=[('c1', '6'),('c2', '7-8'),('c3', '9-12')])
    f = RadioField('Number of steps walked down', validators=[InputRequired()], choices=[('c1', '6'),('c2', '7-8'),('c3', '9-12')])
    g = RadioField('Number of times the user stumbled while ascending the stairs.', validators=[InputRequired()], choices=[('c1', '0-1'),('c2', '2-5'),('c3', '>5')])
    h = RadioField('Number of times the user stumbled while descending the stairs.', validators=[InputRequired()], choices=[('c1', '0-1'),('c2', '2-5'),('c3', '>5')])
    i = RadioField('Is the crutch used during the test?', validators=[InputRequired()], choices=[('c1', 'No'), ('c2', 'Yes')])
    j = RadioField('In general, is the torso bent forward (provoke high load of upper limbs when crutches are used) to avoid falling backwards?', validators=[InputRequired()], choices=[('c1', 'No'), ('c2', 'Yes')])
    k = RadioField('During the Anterolateral shifting of body centre of gravity, is the swing leg adequately relieved to correctly initiate the stride?', validators=[InputRequired()], choices=[('c1', 'Yes'), ('c2', 'No')])
    l = RadioField('Number of error messages sent by the HMI (Human-Machine Interface)', validators=[InputRequired()], choices=[('c1', '0-1'),('c2', '2-3'),('c3', '>3')])
    m = RadioField('Number of times the safe mode has been activated (the system switched off) when the situation did not require it?', validators=[InputRequired()], choices=[('c1', '0-1'),('c2', '2-3'),('c3', '>3')])
    n = RadioField('Has the safe mode not been activated (the system did not switch off) when the situation did require it?', validators=[InputRequired()], choices=[('c1', 'No'), ('c2', 'Yes')])
    submit = SubmitField(label='Submit')