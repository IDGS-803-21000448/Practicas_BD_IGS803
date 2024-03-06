from wtforms import Form
from wtforms import StringField, TelField, SelectField,RadioField, EmailField, IntegerField, FloatField, SelectMultipleField
from wtforms import validators
from wtforms.widgets import ListWidget, CheckboxInput


class UsersForm(Form):
    nombre=StringField('nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa un nombre valido')
    ])
    apaterno=StringField('apaterno', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=15, message='Ingresa un apellido paterno valido')
    ])
    amaterno=StringField('amaterno', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=15, message='Ingresa un apellido materno valido')
    ])
    edad = IntegerField('edad', [
        validators.DataRequired(message='El campo es requerido'),
        validators.number_range(min = 1, max=20, message = "Ingrese Una edad Valido")
    ])
    correo = EmailField('correo', [
        validators.Email(message='Ingrese un correo valido')
    ])

# NOMBRE, CORREO, TELEFONO, DIRECCION, SUELDO
class EmpForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=50, message='Ingresa un nombre valido')
    ])
    email = EmailField('correo', [
        validators.Email(message='Ingrese un correo valido')
    ])
    telefono=StringField('telefono', [
        validators.DataRequired(message='El campo es requerido'),
      validators.length(min=4, max=10, message='Ingresa un nombre valido')
    ])
    direccion=StringField('direccion', [
        validators.DataRequired(message='El campo es requerido'),
      validators.length(min=4, max=50, message='Ingresa un nombre valido')
    ])
    sueldo=FloatField('sueldo', [
        validators.DataRequired(message='El campo es requerido'),
    ])


class PedidoForm(Form):
    cliente_nombre = StringField('Nombre del Cliente', validators=[
        validators.DataRequired(message='Este campo es requerido'),
        validators.Length(min=4, max=100, message='Ingresa un nombre válido')
    ])
    cliente_direccion = StringField('Dirección', validators=[
        validators.DataRequired(message='Este campo es requerido'),
        validators.Length(min=4, max=100, message='Ingresa una dirección válida')
    ])
    cliente_telefono = TelField('Teléfono', validators=[
        validators.DataRequired(message='Este campo es requerido'),
        validators.Length(min=7, max=15, message='Ingresa un número de teléfono válido')
    ])
    tamano_pizza = RadioField('Tamaño de la Pizza', choices=[
        ('Chica', 'Chica $40'),
        ('Mediana', 'Mediana $80'),
        ('Grande', 'Grande $120')
    ], validators=[validators.DataRequired(message='Selecciona un tamaño')])
    ingredientes = SelectMultipleField('Ingredientes', choices=[
        ('jamon', 'Jamón $10'),
        ('piña', 'Piña $10'),
        ('champiñones', 'Champiñones $10')
    ], validators=[validators.Optional()], widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
    numero_pizzas = IntegerField('Número de Pizzas', validators=[
        validators.DataRequired(message='Este campo es requerido'),
        validators.NumberRange(min=1, message='Ingresa un número válido de pizzas')
    ])
    total = FloatField('Total', validators=[validators.Optional()])
