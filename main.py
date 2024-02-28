from flask import Flask, render_template, request, Response
import forms
from flask import g
from flask import flash
from flask import redirect
from flask_wtf import CSRFProtect
from config import DevelopmentConfig
from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
#-------------------------------
 
@app.route("/index",methods=["GET", "POST"])
def index():
    alum_form = forms.UsersForm2(request.form)
    if request.method == "POST":
        alumn = Alumnos(nombre = alum_form.nombre.data
                        ,apaterno = alum_form.apaterno.data
                        ,email = alum_form.email.data)
        
        db.session.add(alumn)
        db.session.commit()


    return render_template("index.html", form = alum_form)

@app.route("/ABC_Completo",methods=["GET", "POST"])
def ABC_Completo():
    alum_form = forms.UsersForm2(request.form)
    alumno = Alumnos.query.all()

    return render_template("ABC_Completo.html", alumnos=alumno)

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    nom = ''
    apa = ''
    ama = ''
    alum_form = forms.UsersForm(request.form)
    if request.method == "POST" and alum_form.validate():
        nom = alum_form.nombre.data
        apa = alum_form.apaterno.data
        ama = alum_form.amaterno.data

        mensaje = f"Bienvenido {nom}"
        flash(mensaje)
    
    return render_template("alumnos.html",
                            form = alum_form,
                            nom=nom, apa=apa, ama=ama)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        
    app.run()
