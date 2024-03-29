from flask import Flask, render_template, request, Response
import forms
from flask import g
from flask import flash
from flask import redirect
from flask_wtf import CSRFProtect
from config import DevelopmentConfig
from models import db
from models import Empleado, Pedido
from flask import request, jsonify
from datetime import datetime
import calendar
from sqlalchemy import func
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

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




@app.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    emp_form = forms.EmpForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        emp1 = db.session.query(Empleado).filter(Empleado.id == id).first()
        emp_form.id.data = request.args.get('id')
        emp_form.nombre.data = emp1.nombre
        emp_form.telefono.data = emp1.telefono
        emp_form.direccion.data = emp1.direccion
        emp_form.sueldo.data = emp1.sueldo
        emp_form.email.data = emp1.email
    if request.method == "POST" and emp_form.validate():
        id = emp_form.id.data
        alum = Empleado.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect('ABC_Completo')
    return render_template("eliminar.html",
                            form = emp_form)

@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    emp_form = forms.EmpForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        emp1 = db.session.query(Empleado).filter(Empleado.id == id).first()
        emp_form.id.data = request.args.get('id')
        emp_form.nombre.data = emp1.nombre
        emp_form.telefono.data = emp1.telefono
        emp_form.direccion.data = emp1.direccion
        emp_form.sueldo.data = emp1.sueldo
        emp_form.email.data = emp1.email
    if request.method == "POST" and emp_form.validate():
        id = emp_form.id.data
        emp = db.session.query(Empleado).filter(Empleado.id == id).first()
        emp.nombre = emp_form.nombre.data
        emp.telefono = emp_form.telefono.data
        emp.direccion = emp_form.direccion.data
        emp.sueldo = emp_form.sueldo.data
        emp.email =  emp_form.email.data
        db.session.add(emp)
        db.session.commit()
        return redirect('ABC_Completo')
    return render_template("modificar.html",
                            form = emp_form)



@app.route("/pedidos", methods=["POST", "GET"])
def agregar_pedido():
    pedido_form = forms.PedidoForm(request.form)
    if request.method == "POST" and pedido_form.validate():
        print("Entra aqui")
        nuevo_pedido = Pedido(
            cliente_nombre=pedido_form.cliente_nombre.data,
            cliente_direccion=pedido_form.cliente_direccion.data,
            cliente_telefono=pedido_form.cliente_telefono.data,
            total=float(pedido_form.total.data),
            fecha_compra= pedido_form.fecha_compra.data
        )

        db.session.add(nuevo_pedido)
        db.session.commit()

        mensaje = "Pedido agregado correctamente"
        flash(mensaje)
        return render_template("pedido.html", form=pedido_form)
    elif request.method == 'GET':
        return render_template("pedido.html", form=pedido_form)
    return render_template("pedido.html", form=pedido_form)


@app.route("/lista_pedidos", methods=["GET"])
def obtener_pedidos():
    tipo_filtro = request.args.get('tipo_filtro')
    filtro_fecha = request.args.get('filtro_fecha')
    filtro_mes = request.args.get('filtro_mes')
    pedidos = None

    if tipo_filtro == 'dia' and filtro_fecha:
        fecha_filtro = datetime.strptime(filtro_fecha, "%Y-%m-%d").date()
        dia_semana_filtro = (fecha_filtro.weekday() + 1) % 7 + 1
        pedidos = Pedido.query.filter(func.dayofweek(Pedido.fecha_compra) == dia_semana_filtro).all()
    elif tipo_filtro == 'mes' and filtro_mes:
        mes = int(filtro_mes.split('-')[1])
        pedidos = Pedido.query.filter(func.month(Pedido.fecha_compra) == mes).all()
    else:
        pedidos = Pedido.query.all()

    suma_totales = sum(pedido.total for pedido in pedidos)
    return render_template("ABC_Pedido.html", pedidos=pedidos, suma_totales=suma_totales)

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        
    app.run()
