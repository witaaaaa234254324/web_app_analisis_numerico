# 🚀 Guía Rápida para Subir a GitHub

## Paso 1: Crear Repositorio en GitHub

1. Ve a https://github.com
2. Click en "New repository" (botón verde)
3. Nombre: `analisis-numerico-web-app` (o el que prefieras)
4. Descripción: `Aplicación web de métodos numéricos - INF-133`
5. Público o Privado (tu elección)
6. **NO** inicializar con README (ya tienes uno)
7. Click en "Create repository"

## Paso 2: Configurar Git Localmente

Abre PowerShell en la carpeta del proyecto:

```powershell
cd "c:\Users\julio\OneDrive\Escritorio\analisis numerico\INF-133\Semana11\web_app_rol_dulceria"
```

### Inicializar Git (si no está inicializado)

```powershell
git init
```

### Agregar todos los archivos

```powershell
git add .
```

### Hacer el primer commit

```powershell
git commit -m "Initial commit: Aplicación web de Análisis Numérico completa"
```

## Paso 3: Conectar con GitHub

Reemplaza `TU-USUARIO` con tu usuario de GitHub:

```powershell
git remote add origin https://github.com/TU-USUARIO/analisis-numerico-web-app.git
```

### Subir el código

```powershell
git branch -M main
git push -u origin main
```

Si te pide autenticación:
- Usuario: tu username de GitHub
- Contraseña: tu Personal Access Token (no tu contraseña normal)

### Crear Personal Access Token (si es necesario)

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Seleccionar: `repo` (todos los permisos de repositorio)
4. Generate token
5. **COPIAR Y GUARDAR** el token (no se volverá a mostrar)
6. Usar ese token como contraseña en git

## Paso 4: Verificar

Ve a tu repositorio en GitHub y verifica que todos los archivos estén subidos.

## Comandos Git Útiles

### Ver el estado actual
```powershell
git status
```

### Ver archivos que se subirán
```powershell
git diff
```

### Agregar cambios nuevos
```powershell
git add .
git commit -m "Descripción de los cambios"
git push
```

### Ver historial de commits
```powershell
git log --oneline
```

## Estructura que Deberías Ver en GitHub

```
analisis-numerico-web-app/
├── .gitignore
├── README.md
├── DEPLOY.md
├── PROYECTO_FINAL.md
├── requirements.txt
├── Procfile
├── runtime.txt
├── init.ps1
└── app/
    ├── controllers/
    ├── models/
    ├── views/
    ├── templates/
    ├── utils/
    ├── database.py
    └── run.py
```

## ⚠️ Archivos que NO se subirán (en .gitignore)

- `__pycache__/`
- `*.pyc`
- `instance/` (base de datos)
- `venv/`
- `.env`

Estos archivos son locales y no deben estar en el repositorio.

## 📝 Actualizar el README.md con tu información

Antes de subir, puedes editar el README.md para agregar:
- Tu nombre
- Enlace al proyecto desplegado (cuando lo despliegues)
- Capturas de pantalla (opcional)

## 🌐 Después de Subir a GitHub

1. Copia el enlace de tu repositorio
2. Ve a Render.com o PythonAnywhere
3. Conecta tu repositorio
4. Deploy automático
5. Obtén el enlace de tu app en producción
6. Agrega ese enlace al README.md

## Comandos Completos en Secuencia

```powershell
# 1. Ir a la carpeta del proyecto
cd "c:\Users\julio\OneDrive\Escritorio\analisis numerico\INF-133\Semana11\web_app_rol_dulceria"

# 2. Inicializar git (si no está inicializado)
git init

# 3. Configurar usuario (primera vez)
git config user.name "Tu Nombre"
git config user.email "tuemail@example.com"

# 4. Agregar archivos
git add .

# 5. Commit inicial
git commit -m "Initial commit: Aplicación de Análisis Numérico completa"

# 6. Conectar con GitHub (reemplaza TU-USUARIO)
git remote add origin https://github.com/TU-USUARIO/analisis-numerico-web-app.git

# 7. Subir
git branch -M main
git push -u origin main
```

## 🎉 ¡Listo!

Tu código ahora está en GitHub y listo para:
- ✅ Compartir con el profesor
- ✅ Desplegarlo en producción
- ✅ Mostrarlo en tu portafolio
- ✅ Colaborar con otros

## Enlaces Importantes

- **GitHub**: https://github.com
- **Documentación Git**: https://git-scm.com/doc
- **Render Deploy**: https://render.com
- **PythonAnywhere**: https://www.pythonanywhere.com

---

**¿Problemas con Git?**

Si tienes errores, intenta:
```powershell
git config --global http.postBuffer 524288000
git remote set-url origin https://github.com/TU-USUARIO/analisis-numerico-web-app.git
```
