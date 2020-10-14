from flask_wtf import FlaskForm
from wtforms import FloatField, DecimalField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from wtforms.widgets import html5 as h5widgets


class BissectionForm(FlaskForm):
    down_limit = FloatField('Limite inferior', 
    validators=[DataRequired(message='Campo não informado.')],
    widget=h5widgets.NumberInput(step=1e-3),
    render_kw={'placeholder': 'Digite o valor do limite infeior'}
    )
    
    upper_limit = FloatField('Limite superior', 
    validators=[DataRequired(message='Campo não informado.')],
    widget=h5widgets.NumberInput(step=1e-3),
    render_kw={'placeholder': 'Digite o valor do limite superior'}
    )
    
    precision = DecimalField('Precisão', 
    validators=[
        NumberRange(
            min=0, 
            max=1, 
            message='Informe uma valor de precisão acima de 0 até 1.'
        )],
        # default=1e-3,
    widget=h5widgets.NumberInput(min=0, max=1, step=1e-12),
    render_kw={'placeholder': 'Digite o valor da precisão desejada'}
    )

    def validate_precision(self, precision):
        if precision.data < 0:
            raise ValidationError("O valor da precisão não pode ser negativo.")

    def validate_upper_limit(self, upper_limit):
        if upper_limit.data < self.down_limit.data:
            raise ValidationError("O valor do limite superior não por ser menor que o limite inferior.")
        elif upper_limit.data == self.down_limit.data:
            raise ValidationError("O valor do limite superior não pode ser igual ao valor do limite inferior.")

    def validate_down_limit(self, down_limit):
        if down_limit.data > self.upper_limit.data:
            raise ValidationError("O valor do limite inferior não por ser maior que o limite superior.")
        elif down_limit.data == self.upper_limit.data:
            raise ValidationError("O valor do limite inferior não pode ser igual ao valor do limite superior.")
    