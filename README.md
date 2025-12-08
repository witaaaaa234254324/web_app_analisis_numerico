# 📊 Análisis Numérico - Aplicación Web

Aplicación web desarrollada con Flask para resolver problemas de Análisis Numérico.

## 🎯 Métodos Implementados

### 1. Gradiente Conjugado (CG)
- Resolución de sistemas lineales Ax = b
- Matrices simétricas positivas definidas
- Aplicación: Análisis estructural, optimización, ecuaciones de calor

### 2. Sobre-relajación Sucesiva (SOR)
- Resolución de sistemas lineales con convergencia acelerada
- Parámetro de relajación ω ajustable
- Aplicación: Ecuaciones diferenciales parciales, problemas de fluidos

### 3. Raíces de Ecuaciones
- **Newton-Raphson**: Convergencia cuadrática
- **Bisección**: Método robusto con garantía de convergencia
- **Secante**: Sin necesidad de derivadas
- Aplicación: Puntos de equilibrio, diseño de circuitos

### 4. Interpolación
- **Lagrange**: Polinomios directos
- **Newton**: Diferencias divididas
- **Splines Cúbicos**: Curvas suaves
- Aplicación: Predicción de datos, procesamiento de señales

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio o descargar el proyecto**

2. **Crear un entorno virtual (recomendado)**
```powershell
cd web_app_rol_dulceria
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. **Instalar dependencias**
```powershell
pip install -r requirements.txt
```

4. **Inicializar la base de datos**
```powershell
cd app
python
```
En el intérprete de Python:
```python
from run import app, db
from models.user_model import User
with app.app_context():
    db.create_all()
    # Crear usuario admin por defecto
    admin = User("Admin", "Sistema", "admin", "admin123", role="admin")
    admin.save()
    # Crear usuario normal
    user = User("Usuario", "Demo", "user", "user123", role="user")
    user.save()
    print("Base de datos inicializada")
exit()
```

5. **Ejecutar la aplicación**
```powershell
python run.py
```

6. **Abrir en el navegador**
```
http://127.0.0.1:5000
```

## 👤 Usuarios por Defecto

| Usuario | Contraseña | Rol |
|---------|------------|-----|
| admin | admin123 | Administrador |
| user | user123 | Usuario |

## 📁 Estructura del Proyecto

```
app/
├── controllers/          # Controladores (lógica de rutas)
│   ├── user_controller.py
│   ├── dul_controller.py
│   └── method_controller.py
├── models/              # Modelos de base de datos
│   ├── user_model.py
│   ├── dul_model.py
│   └── problem_model.py
├── views/               # Vistas (renderizado de templates)
│   ├── user_view.py
│   ├── dul_view.py
│   └── method_view.py
├── templates/           # Plantillas HTML
│   ├── base.html
│   ├── metodos_index.html
│   ├── gradiente_conjugado.html
│   ├── sor.html
│   ├── raices.html
│   ├── interpolacion.html
│   └── ...
├── utils/               # Utilidades
│   ├── decorators.py
│   └── numerical_methods.py
├── database.py          # Configuración de base de datos
└── run.py              # Archivo principal
```

## 🔧 Funcionalidades

### Para Usuarios
- ✅ Resolver problemas con 4 métodos numéricos
- ✅ Guardar automáticamente todos los cálculos
- ✅ Ver historial de problemas resueltos
- ✅ Ver detalles completos de cada solución
- ✅ Perfil de usuario personalizado

### Para Administradores
- ✅ Todas las funcionalidades de usuario
- ✅ Gestionar usuarios (crear, editar, eliminar)
- ✅ Ver historial completo de todos los usuarios
- ✅ Acceso a panel de administración

## 📊 Ejemplos de Uso

### Gradiente Conjugado
```
Matriz A: [[4, 1, 0], [1, 3, 1], [0, 1, 2]]
Vector b: [1, 2, 3]
Tolerancia: 1e-6
```

### SOR
```
Matriz A: [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
Vector b: [6, 25, -11]
Omega (ω): 1.5
```

### Raíces de Ecuaciones
```
Función: x**3 - 2*x - 5
Método: Newton-Raphson
Punto inicial: 2
```

### Interpolación
```
Puntos X: [0, 2, 4, 6, 8]
Puntos Y: [20, 25, 28, 26, 22]
Método: Lagrange
Evaluar en: 5
```

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask 3.0.0
- **Base de Datos**: SQLite con SQLAlchemy
- **Autenticación**: Flask-Login
- **Frontend**: Bulma CSS Framework
- **Cálculos**: NumPy, SciPy
- **Seguridad**: Werkzeug (hash de contraseñas)

## 📝 Notas Importantes

1. La base de datos se crea automáticamente en `instance/analisis_numerico.db`
2. Todos los cálculos se guardan en el historial del usuario
3. Los usuarios solo pueden ver y eliminar sus propios problemas
4. Los administradores tienen acceso completo a todos los datos
5. Las funciones para raíces de ecuaciones usan sintaxis Python (**, *, np.sin, np.exp, etc.)

## 🎓 Materia

**INF-133 - Análisis Numérico**

Trabajo Práctico: Aplicación Web de Métodos Numéricos

## 🚀 Deploy en Producción

Para desplegar en un servidor web (Heroku, PythonAnywhere, etc.), asegúrate de:

1. Configurar variables de entorno para SECRET_KEY
2. Usar una base de datos más robusta (PostgreSQL, MySQL)
3. Configurar HTTPS
4. Ajustar DEBUG=False en producción

## 📧 Soporte

Para problemas o consultas sobre la aplicación, revisar la documentación de Flask y las librerías utilizadas.

---

**Desarrollado con ❤️ para INF-133**
