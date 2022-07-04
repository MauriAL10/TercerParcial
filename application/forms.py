from wtforms import TextAreaField, SubmitField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length

from . import utils

languages_choice = []
for key, value in utils.languages.items():
    languages_choice.append((key, value))
    


class MyForm(FlaskForm):
    data_field = TextAreaField('Texto', 
                            validators=[DataRequired(), 
                            Length(min=1, max=250)]
    )
    language = SelectField("Idioma a traducir", choices=languages_choice)
    submit = SubmitField('Traducir') 