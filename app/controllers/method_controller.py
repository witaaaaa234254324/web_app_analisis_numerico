from flask import Blueprint, request, redirect, url_for, flash, jsonify, render_template
from flask_login import login_required, current_user
import json
import numpy as np

from utils.numerical_methods import (
    gradiente_conjugado, sor, newton_raphson, biseccion, secante,
    interpolacion_lagrange, interpolacion_newton, interpolacion_spline_cubico
)
from models.problem_model import Problem
from views import method_view

method_bp = Blueprint("method", __name__)


# ============================================================================
# PÁGINA PRINCIPAL - Métodos Numéricos
# ============================================================================

@method_bp.route("/metodos")
@login_required
def index():
    """Página principal con descripción de métodos disponibles"""
    return method_view.metodos_index()


@method_bp.route("/historial")
@login_required
def historial():
    """Muestra el historial de problemas resueltos por el usuario"""
    if current_user.has_role("admin"):
        problems = Problem.get_all()
    else:
        problems = Problem.get_by_user(current_user.id)
    return method_view.historial(problems)


@method_bp.route("/historial/<int:id>")
@login_required
def ver_problema(id):
    """Ver detalles de un problema específico"""
    problem = Problem.get_by_id(id)
    if not problem:
        flash("Problema no encontrado", "error")
        return redirect(url_for("method.historial"))
    
    # Verificar permisos
    if not current_user.has_role("admin") and problem.user_id != current_user.id:
        flash("No tienes permiso para ver este problema", "error")
        return redirect(url_for("method.historial"))
    
    return method_view.ver_problema(problem)


@method_bp.route("/historial/<int:id>/delete")
@login_required
def delete_problema(id):
    """Eliminar un problema del historial"""
    problem = Problem.get_by_id(id)
    if not problem:
        flash("Problema no encontrado", "error")
        return redirect(url_for("method.historial"))
    
    # Verificar permisos
    if not current_user.has_role("admin") and problem.user_id != current_user.id:
        flash("No tienes permiso para eliminar este problema", "error")
        return redirect(url_for("method.historial"))
    
    problem.delete()
    flash("Problema eliminado exitosamente", "success")
    return redirect(url_for("method.historial"))


# ============================================================================
# GRADIENTE CONJUGADO
# ============================================================================

@method_bp.route("/gradiente-conjugado", methods=["GET", "POST"])
@login_required
def gradiente_conjugado_view():
    if request.method == "POST":
        try:
            # Obtener datos del formulario
            title = request.form.get("title", "Gradiente Conjugado")
            matriz_str = request.form["matriz"]
            vector_str = request.form["vector"]
            tol = float(request.form.get("tolerancia", 1e-6))
            max_iter = int(request.form.get("max_iter", 1000))
            
            # Parsear matriz y vector
            A = np.array(json.loads(matriz_str))
            b = np.array(json.loads(vector_str))
            
            # Validar que A sea cuadrada
            if A.shape[0] != A.shape[1]:
                flash("La matriz debe ser cuadrada", "error")
                return redirect(url_for("method.gradiente_conjugado_view"))
            
            # Validar dimensiones
            if len(b) != A.shape[0]:
                flash("Las dimensiones de la matriz y el vector no coinciden", "error")
                return redirect(url_for("method.gradiente_conjugado_view"))
            
            # Resolver
            resultado = gradiente_conjugado(A, b, tol=tol, max_iter=max_iter)
            
            # Guardar en BD
            input_data = json.dumps({
                "matriz": A.tolist(),
                "vector": b.tolist(),
                "tolerancia": tol,
                "max_iter": max_iter
            })
            result_data = json.dumps(resultado)
            
            problem = Problem(
                user_id=current_user.id,
                method_type="CG",
                input_data=input_data,
                result_data=result_data,
                title=title
            )
            problem.save()
            
            flash("Problema resuelto exitosamente", "success")
            return method_view.resultado_cg(resultado, A.tolist(), b.tolist())
            
        except Exception as e:
            flash(f"Error al resolver: {str(e)}", "error")
            return redirect(url_for("method.gradiente_conjugado_view"))
    
    return method_view.gradiente_conjugado_form()


# ============================================================================
# SOR (Successive Over-Relaxation)
# ============================================================================

@method_bp.route("/sor", methods=["GET", "POST"])
@login_required
def sor_view():
    if request.method == "POST":
        try:
            title = request.form.get("title", "Método SOR")
            matriz_str = request.form["matriz"]
            vector_str = request.form["vector"]
            omega = float(request.form.get("omega", 1.5))
            tol = float(request.form.get("tolerancia", 1e-6))
            max_iter = int(request.form.get("max_iter", 1000))
            
            # Parsear matriz y vector
            A = np.array(json.loads(matriz_str))
            b = np.array(json.loads(vector_str))
            
            # Validaciones
            if A.shape[0] != A.shape[1]:
                flash("La matriz debe ser cuadrada", "error")
                return redirect(url_for("method.sor_view"))
            
            if len(b) != A.shape[0]:
                flash("Las dimensiones no coinciden", "error")
                return redirect(url_for("method.sor_view"))
            
            # Resolver
            resultado = sor(A, b, omega=omega, tol=tol, max_iter=max_iter)
            
            # Guardar en BD
            input_data = json.dumps({
                "matriz": A.tolist(),
                "vector": b.tolist(),
                "omega": omega,
                "tolerancia": tol,
                "max_iter": max_iter
            })
            result_data = json.dumps(resultado)
            
            problem = Problem(
                user_id=current_user.id,
                method_type="SOR",
                input_data=input_data,
                result_data=result_data,
                title=title
            )
            problem.save()
            
            flash("Problema resuelto exitosamente", "success")
            return method_view.resultado_sor(resultado, A.tolist(), b.tolist())
            
        except Exception as e:
            flash(f"Error al resolver: {str(e)}", "error")
            return redirect(url_for("method.sor_view"))
    
    return method_view.sor_form()


# ============================================================================
# RAÍCES DE ECUACIONES
# ============================================================================

@method_bp.route("/raices", methods=["GET", "POST"])
@login_required
def raices_view():
    if request.method == "POST":
        try:
            title = request.form.get("title", "Raíces de Ecuaciones")
            metodo = request.form["metodo"]
            funcion = request.form["funcion"]
            tol = float(request.form.get("tolerancia", 1e-6))
            max_iter = int(request.form.get("max_iter", 100))
            
            resultado = None
            input_data = {
                "funcion": funcion,
                "metodo": metodo,
                "tolerancia": tol,
                "max_iter": max_iter
            }
            
            if metodo == "newton":
                x0 = float(request.form["x0"])
                input_data["x0"] = x0
                resultado = newton_raphson(funcion, x0, tol, max_iter)
                
            elif metodo == "biseccion":
                a = float(request.form["a"])
                b = float(request.form["b"])
                input_data["a"] = a
                input_data["b"] = b
                resultado = biseccion(funcion, a, b, tol, max_iter)
                
            elif metodo == "secante":
                x0 = float(request.form["x0"])
                x1 = float(request.form["x1"])
                input_data["x0"] = x0
                input_data["x1"] = x1
                resultado = secante(funcion, x0, x1, tol, max_iter)
            
            if resultado:
                # Guardar en BD
                problem = Problem(
                    user_id=current_user.id,
                    method_type="ROOTS",
                    input_data=json.dumps(input_data),
                    result_data=json.dumps(resultado),
                    title=title
                )
                problem.save()
                
                flash("Problema resuelto exitosamente", "success")
                return method_view.resultado_raices(resultado, funcion, metodo)
            
        except Exception as e:
            flash(f"Error al resolver: {str(e)}", "error")
            return redirect(url_for("method.raices_view"))
    
    return method_view.raices_form()


# ============================================================================
# INTERPOLACIÓN
# ============================================================================

@method_bp.route("/interpolacion", methods=["GET", "POST"])
@login_required
def interpolacion_view():
    if request.method == "POST":
        try:
            title = request.form.get("title", "Interpolación")
            metodo = request.form["metodo"]
            x_points_str = request.form["x_points"]
            y_points_str = request.form["y_points"]
            x_eval = request.form.get("x_eval", None)
            
            # Parsear puntos
            x_points = json.loads(x_points_str)
            y_points = json.loads(y_points_str)
            
            if len(x_points) != len(y_points):
                flash("Los vectores X e Y deben tener la misma longitud", "error")
                return redirect(url_for("method.interpolacion_view"))
            
            if x_eval:
                x_eval = float(x_eval)
            
            resultado = None
            
            if metodo == "lagrange":
                resultado = interpolacion_lagrange(x_points, y_points, x_eval)
            elif metodo == "newton":
                resultado = interpolacion_newton(x_points, y_points, x_eval)
            elif metodo == "spline":
                resultado = interpolacion_spline_cubico(x_points, y_points)
                if x_eval:
                    # Evaluar spline en x_eval usando numpy
                    from scipy.interpolate import CubicSpline
                    cs = CubicSpline(x_points, y_points, bc_type='natural')
                    resultado['x_evaluado'] = x_eval
                    resultado['y_evaluado'] = float(cs(x_eval))
            
            if resultado:
                # Guardar en BD
                input_data = json.dumps({
                    "metodo": metodo,
                    "x_points": x_points,
                    "y_points": y_points,
                    "x_eval": x_eval
                })
                result_data = json.dumps(resultado)
                
                problem = Problem(
                    user_id=current_user.id,
                    method_type="INTERPOLATION",
                    input_data=input_data,
                    result_data=result_data,
                    title=title
                )
                problem.save()
                
                flash("Interpolación realizada exitosamente", "success")
                return method_view.resultado_interpolacion(resultado, metodo)
            
        except Exception as e:
            flash(f"Error al interpolar: {str(e)}", "error")
            return redirect(url_for("method.interpolacion_view"))
    
    return method_view.interpolacion_form()
