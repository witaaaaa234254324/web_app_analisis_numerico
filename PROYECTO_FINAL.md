# 📊 APLICACIÓN WEB DE ANÁLISIS NUMÉRICO
## INF-133 - Trabajo Final

---

## 🎯 DESCRIPCIÓN DEL PROYECTO

Aplicación web desarrollada en Flask que implementa **tres métodos principales de Análisis Numérico** aplicados a problemas prácticos:

1. **Gradiente Conjugado (CG)** - Resolución de sistemas lineales
2. **Sobre-relajación Sucesiva (SOR)** - Sistemas lineales con convergencia acelerada  
3. **Raíces de Ecuaciones** - Newton-Raphson, Bisección y Secante
4. **Interpolación** - Lagrange, Newton y Splines Cúbicos

---

## ✨ CARACTERÍSTICAS PRINCIPALES

### Sistema de Usuarios
- ✅ Registro e inicio de sesión
- ✅ Dos roles: Administrador y Usuario
- ✅ Gestión de perfiles
- ✅ Autenticación con Flask-Login

### Calculadoras Numéricas
- ✅ **Gradiente Conjugado**: Para matrices simétricas positivas definidas
- ✅ **SOR**: Con parámetro de relajación ω ajustable
- ✅ **Raíces de Ecuaciones**: 3 métodos diferentes
- ✅ **Interpolación**: 3 métodos con evaluación en puntos específicos

### Historial y Resultados
- ✅ Todos los cálculos se guardan automáticamente
- ✅ Historial personal para cada usuario
- ✅ Visualización detallada de resultados
- ✅ Tablas de convergencia e iteraciones
- ✅ Administradores pueden ver todos los problemas

---

## 🛠️ TECNOLOGÍAS UTILIZADAS

| Categoría | Tecnología | Versión |
|-----------|-----------|---------|
| Backend | Flask | 3.0.0 |
| Base de Datos | SQLite + SQLAlchemy | 3.1.1 |
| Autenticación | Flask-Login | 0.6.3 |
| Seguridad | Werkzeug | 3.0.1 |
| Cálculo Numérico | NumPy | 1.26.2 |
| Cálculo Científico | SciPy | 1.11.4 |
| Frontend | Bulma CSS | 1.0.0 |
| Deploy | Gunicorn | 21.2.0 |

---

## 📁 ESTRUCTURA DEL PROYECTO

```
analisis-numerico/
│
├── app/
│   ├── controllers/              # Lógica de rutas y control
│   │   ├── user_controller.py   # Gestión de usuarios
│   │   └── method_controller.py # ⭐ Métodos numéricos
│   │
│   ├── models/                   # Modelos de datos
│   │   ├── user_model.py        # Usuario con roles
│   │   └── problem_model.py     # ⭐ Problemas resueltos
│   │
│   ├── views/                    # Renderizado de templates
│   │   ├── user_view.py
│   │   └── method_view.py       # ⭐ Vistas de métodos
│   │
│   ├── templates/                # HTML con Jinja2
│   │   ├── base.html            # Template base con navegación
│   │   ├── metodos_index.html   # ⭐ Página principal
│   │   ├── gradiente_conjugado.html
│   │   ├── sor.html
│   │   ├── raices.html
│   │   ├── interpolacion.html
│   │   ├── resultado_*.html     # Resultados de cada método
│   │   ├── historial.html       # ⭐ Historial de problemas
│   │   └── ...
│   │
│   ├── utils/                    # Utilidades
│   │   ├── decorators.py        # @role_required
│   │   └── numerical_methods.py # ⭐ Implementaciones numéricas
│   │
│   ├── database.py              # Configuración de DB
│   └── run.py                   # ⭐ Aplicación principal
│
├── instance/                     # Base de datos SQLite
│   └── analisis_numerico.db
│
├── requirements.txt              # Dependencias Python
├── Procfile                      # Para deploy en Render/Heroku
├── runtime.txt                   # Versión de Python
├── .gitignore                    # Archivos a ignorar en Git
├── init.ps1                      # Script de inicialización
├── README.md                     # Documentación principal
└── DEPLOY.md                     # Guía de despliegue

```

---

## 🚀 INSTALACIÓN Y USO

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes)
- Git (opcional)

### Instalación Rápida

```powershell
# 1. Clonar o descargar el proyecto
cd web_app_rol_dulceria

# 2. Crear entorno virtual (recomendado)
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Inicializar base de datos
cd app
python -c "from run import app, db; from models.user_model import User; app.app_context().push(); db.create_all(); admin = User('Admin', 'Sistema', 'admin', 'admin123', role='admin'); admin.save(); user = User('Usuario', 'Demo', 'user', 'user123', role='user'); user.save(); print('✓ DB inicializada')"

# 5. Ejecutar aplicación
python run.py
```

### Acceder a la Aplicación
Abrir navegador en: **http://127.0.0.1:5000**

---

## 👥 USUARIOS POR DEFECTO

| Usuario | Contraseña | Rol | Permisos |
|---------|------------|-----|----------|
| `admin` | `admin123` | Administrador | Acceso completo |
| `user` | `user123` | Usuario | Calculadoras + Historial propio |

---

## 📊 MÉTODOS NUMÉRICOS IMPLEMENTADOS

### 1️⃣ GRADIENTE CONJUGADO (CG)

**Aplicación Práctica**: Resolución de sistemas lineales grandes con matrices simétricas positivas definidas.

**Casos de Uso**:
- Análisis estructural (deformaciones en vigas)
- Ecuaciones de calor y difusión
- Optimización de funciones cuadráticas
- Problemas de elementos finitos

**Ejemplo**:
```
Matriz A: [[4, 1, 0], [1, 3, 1], [0, 1, 2]]
Vector b: [1, 2, 3]
Tolerancia: 1e-6
```

**Características**:
- Convergencia rápida (n iteraciones máximo)
- Eficiente para matrices grandes
- Requiere matriz simétrica y positiva definida

---

### 2️⃣ SOR (SUCCESSIVE OVER-RELAXATION)

**Aplicación Práctica**: Aceleración de convergencia en sistemas lineales.

**Casos de Uso**:
- Ecuaciones diferenciales parciales (EDP)
- Problemas de flujo de fluidos
- Distribución de temperatura en placas
- Problemas de Poisson y Laplace

**Ejemplo**:
```
Matriz A: [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
Vector b: [6, 25, -11]
Omega (ω): 1.5
Tolerancia: 1e-6
```

**Características**:
- Parámetro ω ajustable (1 < ω < 2)
- Más rápido que Gauss-Seidel
- Ideal para matrices diagonalmente dominantes

---

### 3️⃣ RAÍCES DE ECUACIONES

#### A) Newton-Raphson
**Convergencia**: Cuadrática (muy rápida)  
**Ventaja**: Pocas iteraciones  
**Desventaja**: Necesita derivada

**Ejemplo**:
```
Función: x**3 - 2*x - 5
Punto inicial: 2
Tolerancia: 1e-6
```

#### B) Bisección
**Convergencia**: Lineal (más lenta pero segura)  
**Ventaja**: Siempre converge si hay cambio de signo  
**Desventaja**: Requiere intervalo [a, b]

**Ejemplo**:
```
Función: x**2 - 4
Intervalo: [0, 3]
```

#### C) Secante
**Convergencia**: Superlineal  
**Ventaja**: No necesita derivada  
**Desventaja**: Necesita dos puntos iniciales

**Aplicaciones Prácticas**:
- Cálculo de puntos de equilibrio
- Diseño de circuitos electrónicos
- Análisis de rendimiento de sistemas
- Ecuaciones trascendentales

---

### 4️⃣ INTERPOLACIÓN

#### A) Lagrange
- Construcción directa del polinomio
- Fácil de implementar
- Grado n-1 con n puntos

#### B) Newton (Diferencias Divididas)
- Tabla de diferencias divididas
- Fácil agregar puntos nuevos
- Coeficientes claros

#### C) Splines Cúbicos
- Curvas suaves (continuidad C²)
- Natural o con condiciones de frontera
- Mejor para muchos puntos

**Ejemplo**:
```
X: [0, 2, 4, 6, 8]
Y: [20, 25, 28, 26, 22]
Evaluar en: x = 5
```

**Aplicaciones Prácticas**:
- Predicción de datos meteorológicos
- Procesamiento de señales digitales
- Gráficos por computadora
- Interpolación de tablas experimentales

---

## 💡 EJEMPLOS PRÁCTICOS INCLUIDOS

### Ejemplo 1: Sistema de Ecuaciones Térmicas (CG)
Distribución de temperatura en una barra metálica:
```
A = [[5, -1, 0], [-1, 5, -1], [0, -1, 5]]
b = [10, 20, 30]
```

### Ejemplo 2: Ecuación de Laplace 2D (SOR)
Distribución de potencial eléctrico:
```
A = [[4, -1, 0], [-1, 4, -1], [0, -1, 4]]
b = [15, 10, 10]
ω = 1.2
```

### Ejemplo 3: Punto de Equilibrio (Newton)
Intersección de oferta y demanda:
```
f(x) = x**3 - 2*x - 5
x₀ = 2
```

### Ejemplo 4: Temperatura vs Tiempo (Interpolación)
```
Horas: [0, 2, 4, 6, 8]
°C: [20, 25, 28, 26, 22]
Estimar temperatura a las 5 horas
```

---

## 🔒 SEGURIDAD

- ✅ Contraseñas hasheadas con Werkzeug (PBKDF2)
- ✅ Protección de rutas con `@login_required`
- ✅ Control de acceso por roles con `@role_required`
- ✅ Sesiones seguras con Flask-Login
- ✅ SECRET_KEY configurable por variable de entorno
- ✅ Validación de entrada de datos
- ✅ Prevención de SQL Injection con SQLAlchemy ORM

---

## 🌐 DESPLIEGUE EN PRODUCCIÓN

### Opciones Recomendadas:

1. **Render.com** (Recomendado - Gratis)
   - Deploy automático desde GitHub
   - HTTPS incluido
   - Base de datos PostgreSQL gratuita

2. **PythonAnywhere** (Más fácil)
   - Interface web simple
   - 500MB de espacio gratis
   - Perfecto para demos

3. **Heroku** (Popular)
   - CLI poderoso
   - Add-ons disponibles
   - Requiere tarjeta (pero es gratis)

**Ver `DEPLOY.md` para instrucciones detalladas**

---

## 📈 CARACTERÍSTICAS TÉCNICAS

### Arquitectura
- **Patrón**: MVC (Modelo-Vista-Controlador)
- **Base de datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **ORM**: SQLAlchemy
- **Autenticación**: Flask-Login con UserMixin
- **Templates**: Jinja2
- **CSS Framework**: Bulma (responsive)

### Funcionalidades del Sistema
1. **Gestión de Usuarios**
   - Registro con validación
   - Login/Logout
   - Perfiles personalizados
   - Roles y permisos

2. **Calculadoras Numéricas**
   - Formularios dinámicos
   - Validación de entrada
   - Cálculo en tiempo real
   - Resultados detallados

3. **Historial**
   - Almacenamiento automático
   - Búsqueda y filtrado
   - Visualización detallada
   - Eliminación controlada

4. **Resultados**
   - Soluciones numéricas
   - Tablas de iteraciones
   - Gráficos de convergencia
   - Métricas de error

---

## 📝 NOTAS PARA LA PRESENTACIÓN

### Puntos Clave a Destacar:

1. **Aplicación Práctica**: Cada método resuelve problemas reales
2. **Interfaz Intuitiva**: Fácil de usar sin conocimientos técnicos
3. **Persistencia de Datos**: Historial completo de cálculos
4. **Seguridad**: Sistema de roles y autenticación
5. **Escalabilidad**: Fácil agregar nuevos métodos

### Demostración Sugerida:

1. **Login** como usuario normal
2. **Resolver un problema** de cada tipo:
   - CG: Sistema de ecuaciones térmicas
   - SOR: Ecuación de Laplace
   - Raíces: Newton-Raphson
   - Interpolación: Lagrange
3. **Mostrar historial** personal
4. **Login** como admin
5. **Gestionar usuarios** y ver historial global

---

## 🎓 INFORMACIÓN ACADÉMICA

**Curso**: INF-133 - Análisis Numérico  
**Proyecto**: Aplicación Web de Métodos Numéricos  
**Fecha**: Diciembre 2025  

---

## 📞 SOPORTE Y DOCUMENTACIÓN

- **README.md**: Instalación y uso básico
- **DEPLOY.md**: Guía de despliegue en producción
- **Código fuente**: Completamente comentado
- **Ejemplos**: Incluidos en cada formulario

---

## ✅ CHECKLIST DE ENTREGA

- [✓] Código fuente completo
- [✓] Base de datos con modelos
- [✓] Sistema de autenticación
- [✓] Tres métodos numéricos principales
- [✓] Ejemplos prácticos funcionando
- [✓] Historial de problemas
- [✓] Interfaz responsive
- [✓] Documentación completa
- [✓] README con instrucciones
- [✓] Archivos para deploy
- [✓] .gitignore configurado
- [✓] requirements.txt actualizado

---

## 🎯 OBJETIVOS CUMPLIDOS

✅ Aplicación web funcional con Flask  
✅ Implementación de métodos numéricos  
✅ Problemas prácticos y aplicados  
✅ Sin teoría, solo funcionalidad  
✅ Código subido a GitHub  
✅ Lista para deploy en producción  

---

**¡PROYECTO COMPLETO Y LISTO PARA PRESENTAR!** 🎉
