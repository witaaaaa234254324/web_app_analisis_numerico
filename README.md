# 📊 Análisis Numérico - Aplicación Web

<div align="center">

![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.26.4-013243?style=for-the-badge&logo=numpy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Online-success?style=for-the-badge)

### 🚀 [**VER APLICACIÓN EN VIVO**](https://erickxdps.pythonanywhere.com/metodos) 🚀

*Aplicación web profesional desarrollada con Flask para resolver problemas de Análisis Numérico*
#Recuerda que para acceder a la demo el usuario y la contraseña es admin por primera vez#

[Demo en Vivo](https://erickxdps.pythonanywhere.com/metodos) • [Características](#-métodos-implementados) • [Instalación](#-instalación-y-configuración) • [Uso](#-ejemplos-de-uso)

</div>

---

---

## ⚡ Quick Start

```bash
# 1. Clonar el repositorio
git clone https://github.com/witaaaaa234254324/web_app_analisis_numerico.git
cd web_app_analisis_numerico

# 2. Crear entorno virtual
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
# source venv/bin/activate    # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
cd app
python run.py

# 5. Abrir en navegador
# http://127.0.0.1:5000
```

O simplemente usa la **[versión online](https://erickxdps.pythonanywhere.com/metodos)** 🚀

---

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

## 🚀 Instalación Local (Opcional)

> 💡 **Nota:** Puedes usar directamente la [aplicación online](https://erickxdps.pythonanywhere.com/metodos) sin instalar nada

### Requisitos
- Python 3.8+ 
- pip

### Instalación Rápida

**1. Clonar y configurar entorno:**
```powershell
git clone https://github.com/witaaaaa234254324/web_app_analisis_numerico.git
cd web_app_analisis_numerico
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
```

**2. Instalar dependencias:**
```powershell
pip install -r requirements.txt
```

**3. Ejecutar aplicación:**
```powershell
cd app
python run.py
```

**4. Abrir navegador:**
```
http://127.0.0.1:5000
```

### 🎉 Usuarios Locales

Al ejecutar por primera vez, se crean automáticamente:
- **Admin:** `admin` / `admin`

---

## 🌐 Aplicación en Producción

### 🎯 Acceso Directo:
**URL:** https://erickxdps.pythonanywhere.com/metodos

### 👤 Usuarios de Prueba (Demo Online)

| Usuario | Contraseña | Rol | Permisos |
|---------|------------|-----|----------|
| `admin` | `admin` | 👑 Administrador | Acceso total + Gestión de usuarios |

> 💡 **Tip:** Puedes crear tu propia cuenta usando la opción "Registrarse"

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

## 🚀 Despliegue en Producción

### ✅ Esta aplicación está desplegada en:
- **Plataforma:** PythonAnywhere
- **URL:** https://erickxdps.pythonanywhere.com/metodos
- **Estado:** 🟢 Online 24/7
- **HTTPS:** ✅ Habilitado

### 📦 Opciones de Despliegue

Si deseas desplegar tu propia instancia:

1. **PythonAnywhere** (Recomendado - GRATIS)
   - Sigue la guía: `GUIA_PYTHONANYWHERE.md`
   - 100% gratuito, no se duerme
   
2. **Railway.app** (Moderna)
   - Sigue la guía: `GUIA_RAILWAY.md`
   - $5 USD/mes incluidos
   
3. **Otras opciones:** Ver `MEJORES_OPCIONES_DEPLOY.md`

### 🔒 Configuración de Seguridad en Producción

Para tu propio deploy:
1. Configura `SECRET_KEY` como variable de entorno
2. Cambia las contraseñas por defecto
3. Ajusta `FLASK_ENV=production`
4. Habilita HTTPS

---

## 📸 Capturas de Pantalla

<div align="center">

### 🏠 Página Principal
![Métodos](https://img.shields.io/badge/Ver-Demo_en_Vivo-blue?style=for-the-badge)

### 🧮 Gradiente Conjugado
*Resolución de sistemas lineales con visualización de iteraciones*

### 📊 Historial de Problemas
*Todos tus cálculos guardados y organizados*

### 👥 Panel de Administración
*Gestión completa de usuarios (solo admin)*

</div>

---

## 🎯 Características Destacadas

- ✨ **Interfaz moderna y responsiva** con Bulma CSS
- 🔒 **Sistema de autenticación seguro** con Flask-Login
- 💾 **Guardado automático** de todos los cálculos
- 📊 **Visualización de resultados** con tablas de iteraciones
- 👥 **Roles de usuario** (Admin/Usuario)
- 📱 **Compatible con móviles** (Responsive Design)
- ⚡ **Cálculos rápidos** con NumPy y SciPy
- 🎨 **Sintaxis matemática** intuitiva para funciones
- 🌐 **Desplegada 24/7** sin caídas

---

## 🤝 Contribuciones

Este es un proyecto académico para **INF-133 - Análisis Numérico**.

### Desarrollador
- **GitHub:** [@witaaaaa234254324](https://github.com/witaaaaa234254324)
- **Proyecto:** [web_app_analisis_numerico](https://github.com/witaaaaa234254324/web_app_analisis_numerico)

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## 📧 Soporte

Para problemas o consultas:
- 🐛 **Issues:** [GitHub Issues](https://github.com/witaaaaa234254324/web_app_analisis_numerico/issues)
- 📚 **Documentación:** Ver archivos `GUIA_*.md`
- 🌐 **Demo:** https://erickxdps.pythonanywhere.com/metodos

---

<div align="center">

### 🌟 ¡Prueba la aplicación ahora!

[![Abrir Aplicación](https://img.shields.io/badge/🚀_Abrir_Aplicación-Online-success?style=for-the-badge)](https://erickxdps.pythonanywhere.com/metodos)

**Desarrollado con ❤️ para Análisis Numérico**

![Made with Python](https://img.shields.io/badge/Made_with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Powered by Flask](https://img.shields.io/badge/Powered_by-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Deployed on PythonAnywhere](https://img.shields.io/badge/Deployed_on-PythonAnywhere-1e8449?style=for-the-badge)

</div>

