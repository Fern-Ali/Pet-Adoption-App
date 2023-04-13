from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, validators, ValidationError
from wtforms.validators import InputRequired, Optional, Email


class addPetForm(FlaskForm):
    """Form for adding/editing friend."""

    name = StringField("Name",
                       validators=[InputRequired()])
    species = StringField("Species",
                        validators=[Optional()])
    photo_url = StringField("Photo URL",
                        validators=[Optional()])
    age = FloatField("Age",
                        validators=[Optional()])
    notes = StringField("Notes",
                        validators=[Optional()])
