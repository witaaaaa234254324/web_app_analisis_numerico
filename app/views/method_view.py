from flask import render_template
from flask_login import current_user
import json


def metodos_index():
    """Página principal de métodos numéricos"""
    return render_template(
        "metodos_index.html",
        title="Métodos Numéricos",
        current_user=current_user
    )


def historial(problems):
    """Historial de problemas resueltos"""
    return render_template(
        "historial.html",
        title="Historial de Problemas",
        problems=problems,
        current_user=current_user
    )


def ver_problema(problem):
    """Ver detalles de un problema específico"""
    input_data = json.loads(problem.input_data)
    result_data = json.loads(problem.result_data)
    
    return render_template(
        "ver_problema.html",
        title=f"Problema: {problem.title}",
        problem=problem,
        input_data=input_data,
        result_data=result_data,
        current_user=current_user
    )


# ============================================================================
# GRADIENTE CONJUGADO
# ============================================================================

def gradiente_conjugado_form():
    """Formulario para Gradiente Conjugado"""
    return render_template(
        "gradiente_conjugado.html",
        title="Gradiente Conjugado (CG)",
        current_user=current_user
    )


def resultado_cg(resultado, matriz, vector):
    """Resultados del Gradiente Conjugado"""
    return render_template(
        "resultado_cg.html",
        title="Resultado - Gradiente Conjugado",
        resultado=resultado,
        matriz=matriz,
        vector=vector,
        current_user=current_user
    )


# ============================================================================
# SOR
# ============================================================================

def sor_form():
    """Formulario para SOR"""
    return render_template(
        "sor.html",
        title="Método SOR",
        current_user=current_user
    )


def resultado_sor(resultado, matriz, vector):
    """Resultados del método SOR"""
    return render_template(
        "resultado_sor.html",
        title="Resultado - SOR",
        resultado=resultado,
        matriz=matriz,
        vector=vector,
        current_user=current_user
    )


# ============================================================================
# RAÍCES DE ECUACIONES
# ============================================================================

def raices_form():
    """Formulario para búsqueda de raíces"""
    return render_template(
        "raices.html",
        title="Raíces de Ecuaciones",
        current_user=current_user
    )


def resultado_raices(resultado, funcion, metodo):
    """Resultados de búsqueda de raíces"""
    return render_template(
        "resultado_raices.html",
        title=f"Resultado - {metodo.upper()}",
        resultado=resultado,
        funcion=funcion,
        metodo=metodo,
        current_user=current_user
    )


# ============================================================================
# INTERPOLACIÓN
# ============================================================================

def interpolacion_form():
    """Formulario para interpolación"""
    return render_template(
        "interpolacion.html",
        title="Interpolación",
        current_user=current_user
    )


def resultado_interpolacion(resultado, metodo):
    """Resultados de interpolación"""
    return render_template(
        "resultado_interpolacion.html",
        title=f"Resultado - Interpolación {metodo.capitalize()}",
        resultado=resultado,
        metodo=metodo,
        current_user=current_user
    )
