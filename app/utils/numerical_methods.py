"""
Implementaciones de métodos numéricos para Análisis Numérico
"""
import numpy as np
from typing import List, Tuple, Callable, Dict, Any


# ============================================================================
# GRADIENTE CONJUGADO (CG) - Resolución de sistemas lineales Ax = b
# ============================================================================

def gradiente_conjugado(A: np.ndarray, b: np.ndarray, x0: np.ndarray = None, 
                       tol: float = 1e-6, max_iter: int = 1000) -> Dict[str, Any]:
    """
    Resuelve el sistema Ax = b usando el método del Gradiente Conjugado.
    
    Args:
        A: Matriz simétrica positiva definida (n x n)
        b: Vector de términos independientes (n)
        x0: Vector inicial (si es None, se usa el vector cero)
        tol: Tolerancia para convergencia
        max_iter: Número máximo de iteraciones
    
    Returns:
        Dict con solución, iteraciones, residuos y error
    """
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    
    x = x0.copy()
    r = b - A @ x
    p = r.copy()
    rs_old = r @ r
    
    iteraciones = []
    residuos = []
    
    for i in range(max_iter):
        Ap = A @ p
        alpha = rs_old / (p @ Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rs_new = r @ r
        
        residuo = np.sqrt(rs_new)
        residuos.append(residuo)
        iteraciones.append(x.copy())
        
        if residuo < tol:
            return {
                'solucion': x.tolist(),
                'iteraciones_totales': i + 1,
                'residuos': residuos,
                'convergencia': True,
                'error_final': residuo,
                'historial_x': [iter_x.tolist() for iter_x in iteraciones]
            }
        
        beta = rs_new / rs_old
        p = r + beta * p
        rs_old = rs_new
    
    return {
        'solucion': x.tolist(),
        'iteraciones_totales': max_iter,
        'residuos': residuos,
        'convergencia': False,
        'error_final': np.sqrt(rs_old),
        'historial_x': [iter_x.tolist() for iter_x in iteraciones]
    }


# ============================================================================
# SOR (Successive Over-Relaxation) - Resolución de sistemas lineales
# ============================================================================

def sor(A: np.ndarray, b: np.ndarray, omega: float = 1.5, x0: np.ndarray = None,
        tol: float = 1e-6, max_iter: int = 1000) -> Dict[str, Any]:
    """
    Resuelve el sistema Ax = b usando el método SOR.
    
    Args:
        A: Matriz de coeficientes (n x n)
        b: Vector de términos independientes (n)
        omega: Factor de relajación (1 < omega < 2 típicamente)
        x0: Vector inicial (si es None, se usa el vector cero)
        tol: Tolerancia para convergencia
        max_iter: Número máximo de iteraciones
    
    Returns:
        Dict con solución, iteraciones, errores y omega usado
    """
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    
    x = x0.copy()
    iteraciones = []
    errores = []
    
    for k in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            suma = 0.0
            for j in range(n):
                if j != i:
                    suma += A[i, j] * x[j]
            
            x[i] = (1 - omega) * x[i] + (omega / A[i, i]) * (b[i] - suma)
        
        error = np.linalg.norm(x - x_old, ord=np.inf)
        errores.append(error)
        iteraciones.append(x.copy())
        
        if error < tol:
            return {
                'solucion': x.tolist(),
                'iteraciones_totales': k + 1,
                'errores': errores,
                'convergencia': True,
                'error_final': error,
                'omega': omega,
                'historial_x': [iter_x.tolist() for iter_x in iteraciones]
            }
    
    return {
        'solucion': x.tolist(),
        'iteraciones_totales': max_iter,
        'errores': errores,
        'convergencia': False,
        'error_final': errores[-1] if errores else None,
        'omega': omega,
        'historial_x': [iter_x.tolist() for iter_x in iteraciones]
    }


# ============================================================================
# RAÍCES DE ECUACIONES
# ============================================================================

def newton_raphson(func_str: str, x0: float, tol: float = 1e-6, 
                   max_iter: int = 100) -> Dict[str, Any]:
    """
    Encuentra la raíz de una función usando el método de Newton-Raphson.
    
    Args:
        func_str: String con la función (ej: "x**3 - 2*x - 5")
        x0: Punto inicial
        tol: Tolerancia
        max_iter: Máximo de iteraciones
    
    Returns:
        Dict con raíz, iteraciones y errores
    """
    # Definir la función y su derivada
    x = x0
    iteraciones = []
    errores = []
    
    # Calcular derivada numéricamente
    h = 1e-8
    
    for i in range(max_iter):
        # Evaluar función
        f_x = eval(func_str.replace('x', f'({x})'))
        
        # Derivada numérica
        f_x_h = eval(func_str.replace('x', f'({x + h})'))
        df_x = (f_x_h - f_x) / h
        
        if abs(df_x) < 1e-12:
            return {
                'raiz': None,
                'iteraciones_totales': i,
                'convergencia': False,
                'error': 'Derivada cercana a cero',
                'historial': iteraciones,
                'errores': errores
            }
        
        x_new = x - f_x / df_x
        error = abs(x_new - x)
        
        iteraciones.append({
            'iteracion': i + 1,
            'x': x,
            'f(x)': f_x,
            'df(x)': df_x,
            'x_new': x_new,
            'error': error
        })
        errores.append(error)
        
        if error < tol:
            return {
                'raiz': x_new,
                'iteraciones_totales': i + 1,
                'convergencia': True,
                'error_final': error,
                'historial': iteraciones,
                'errores': errores,
                'f_raiz': eval(func_str.replace('x', f'({x_new})'))
            }
        
        x = x_new
    
    return {
        'raiz': x,
        'iteraciones_totales': max_iter,
        'convergencia': False,
        'error_final': errores[-1] if errores else None,
        'historial': iteraciones,
        'errores': errores
    }


def biseccion(func_str: str, a: float, b: float, tol: float = 1e-6,
              max_iter: int = 100) -> Dict[str, Any]:
    """
    Encuentra la raíz de una función usando el método de Bisección.
    
    Args:
        func_str: String con la función
        a, b: Extremos del intervalo [a, b]
        tol: Tolerancia
        max_iter: Máximo de iteraciones
    
    Returns:
        Dict con raíz, iteraciones y errores
    """
    # Evaluar en los extremos
    f_a = eval(func_str.replace('x', f'({a})'))
    f_b = eval(func_str.replace('x', f'({b})'))
    
    if f_a * f_b > 0:
        return {
            'raiz': None,
            'convergencia': False,
            'error': 'La función no cambia de signo en el intervalo dado',
            'historial': []
        }
    
    iteraciones = []
    errores = []
    
    for i in range(max_iter):
        c = (a + b) / 2
        f_c = eval(func_str.replace('x', f'({c})'))
        
        error = (b - a) / 2
        
        iteraciones.append({
            'iteracion': i + 1,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': f_c,
            'error': error
        })
        errores.append(error)
        
        if error < tol or abs(f_c) < tol:
            return {
                'raiz': c,
                'iteraciones_totales': i + 1,
                'convergencia': True,
                'error_final': error,
                'historial': iteraciones,
                'errores': errores,
                'f_raiz': f_c
            }
        
        f_a = eval(func_str.replace('x', f'({a})'))
        if f_a * f_c < 0:
            b = c
        else:
            a = c
    
    c = (a + b) / 2
    return {
        'raiz': c,
        'iteraciones_totales': max_iter,
        'convergencia': False,
        'error_final': errores[-1] if errores else None,
        'historial': iteraciones,
        'errores': errores
    }


def secante(func_str: str, x0: float, x1: float, tol: float = 1e-6,
            max_iter: int = 100) -> Dict[str, Any]:
    """
    Encuentra la raíz usando el método de la Secante.
    """
    iteraciones = []
    errores = []
    
    for i in range(max_iter):
        f_x0 = eval(func_str.replace('x', f'({x0})'))
        f_x1 = eval(func_str.replace('x', f'({x1})'))
        
        if abs(f_x1 - f_x0) < 1e-12:
            return {
                'raiz': None,
                'convergencia': False,
                'error': 'División por cero',
                'historial': iteraciones
            }
        
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        error = abs(x2 - x1)
        
        iteraciones.append({
            'iteracion': i + 1,
            'x0': x0,
            'x1': x1,
            'x2': x2,
            'f(x1)': f_x1,
            'error': error
        })
        errores.append(error)
        
        if error < tol:
            return {
                'raiz': x2,
                'iteraciones_totales': i + 1,
                'convergencia': True,
                'error_final': error,
                'historial': iteraciones,
                'errores': errores,
                'f_raiz': eval(func_str.replace('x', f'({x2})'))
            }
        
        x0 = x1
        x1 = x2
    
    return {
        'raiz': x1,
        'iteraciones_totales': max_iter,
        'convergencia': False,
        'error_final': errores[-1] if errores else None,
        'historial': iteraciones,
        'errores': errores
    }


# ============================================================================
# INTERPOLACIÓN
# ============================================================================

def interpolacion_lagrange(x_points: List[float], y_points: List[float], 
                          x_eval: float = None) -> Dict[str, Any]:
    """
    Realiza interpolación de Lagrange.
    
    Args:
        x_points: Lista de puntos x conocidos
        y_points: Lista de puntos y conocidos
        x_eval: Punto donde evaluar el polinomio (opcional)
    
    Returns:
        Dict con coeficientes, polinomio y evaluación
    """
    n = len(x_points)
    
    def L(k, x):
        """Calcula el k-ésimo polinomio base de Lagrange"""
        resultado = 1.0
        for i in range(n):
            if i != k:
                resultado *= (x - x_points[i]) / (x_points[k] - x_points[i])
        return resultado
    
    def P(x):
        """Evalúa el polinomio interpolante en x"""
        resultado = 0.0
        for k in range(n):
            resultado += y_points[k] * L(k, x)
        return resultado
    
    # Generar puntos para graficar
    x_min, x_max = min(x_points), max(x_points)
    x_plot = np.linspace(x_min, x_max, 100)
    y_plot = [P(x) for x in x_plot]
    
    resultado = {
        'tipo': 'Lagrange',
        'grado': n - 1,
        'puntos_x': x_points,
        'puntos_y': y_points,
        'x_grafica': x_plot.tolist(),
        'y_grafica': y_plot
    }
    
    if x_eval is not None:
        resultado['x_evaluado'] = x_eval
        resultado['y_evaluado'] = P(x_eval)
    
    return resultado


def interpolacion_newton(x_points: List[float], y_points: List[float],
                        x_eval: float = None) -> Dict[str, Any]:
    """
    Realiza interpolación usando diferencias divididas de Newton.
    
    Returns:
        Dict con tabla de diferencias divididas, coeficientes y evaluación
    """
    n = len(x_points)
    
    # Tabla de diferencias divididas
    tabla = np.zeros((n, n))
    tabla[:, 0] = y_points
    
    for j in range(1, n):
        for i in range(n - j):
            tabla[i, j] = (tabla[i + 1, j - 1] - tabla[i, j - 1]) / \
                         (x_points[i + j] - x_points[i])
    
    # Coeficientes (primera fila)
    coeficientes = tabla[0, :].tolist()
    
    def P(x):
        """Evalúa el polinomio de Newton en x"""
        resultado = coeficientes[0]
        producto = 1.0
        for k in range(1, n):
            producto *= (x - x_points[k - 1])
            resultado += coeficientes[k] * producto
        return resultado
    
    # Generar puntos para graficar
    x_min, x_max = min(x_points), max(x_points)
    x_plot = np.linspace(x_min, x_max, 100)
    y_plot = [P(x) for x in x_plot]
    
    resultado = {
        'tipo': 'Newton',
        'grado': n - 1,
        'puntos_x': x_points,
        'puntos_y': y_points,
        'coeficientes': coeficientes,
        'tabla_diferencias': tabla.tolist(),
        'x_grafica': x_plot.tolist(),
        'y_grafica': y_plot
    }
    
    if x_eval is not None:
        resultado['x_evaluado'] = x_eval
        resultado['y_evaluado'] = P(x_eval)
    
    return resultado


def interpolacion_spline_cubico(x_points: List[float], y_points: List[float]) -> Dict[str, Any]:
    """
    Realiza interpolación con Splines Cúbicos Naturales.
    """
    from scipy.interpolate import CubicSpline
    
    cs = CubicSpline(x_points, y_points, bc_type='natural')
    
    # Generar puntos para graficar
    x_min, x_max = min(x_points), max(x_points)
    x_plot = np.linspace(x_min, x_max, 200)
    y_plot = cs(x_plot)
    
    return {
        'tipo': 'Spline Cúbico Natural',
        'puntos_x': x_points,
        'puntos_y': y_points,
        'x_grafica': x_plot.tolist(),
        'y_grafica': y_plot.tolist()
    }
