from wtforms import Form
from wtforms import StringField, SelectField,RadioField, EmailField, IntegerField, FloatField
from wtforms import validators



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
    identificador=IntegerField('id')
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