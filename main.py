from flask import Flask, render_template, request, Response
import forms
from flask import g
from flask import flash
from flask import redirect
from flask_wtf import CSRFProtect
from config import DevelopmentConfig
from models import db
from models import Empleado

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
#-------------------------------
 
@app.route("/index",methods=["GET", "POST"])
def index():
    emp_form = forms.EmpForm(request.form)
    if request.method == "POST":
        emp = Empleado(nombre = emp_form.nombre.data
                        ,telefono = emp_form.telefono.data
                        ,email = emp_form.email.data
                        , direccion = emp_form.direccion.data
                        ,sueldo = emp_form.sueldo.data)
        
        db.session.add(emp)
        db.session.commit()


    return render_template("index.html", form = emp_form)

@app.route("/ABC_Completo",methods=["GET", "POST"])
def ABC_Completo():
    emp_form = forms.EmpForm(request.form)
    empleados = Empleado.query.all()

    return render_template("ABC_Completo.html", empleados=empleados)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        
    app.run()
