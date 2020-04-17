from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired


class AreaForm(FlaskForm):
    width = StringField('Width', validators=[DataRequired()])
    height = StringField('Height', validators=[DataRequired()])
    color = SelectField('Color', choices=[('red', 'Red'), ('blue', 'Blue')],
                        validators=[DataRequired()])
    material = SelectField('Material', choices=[('parquet', 'Parquet'), ('wooden', 'Wooden')],
                           validators=[DataRequired()])
    num_of_masters = StringField('Number of masters', validators=[DataRequired()])
