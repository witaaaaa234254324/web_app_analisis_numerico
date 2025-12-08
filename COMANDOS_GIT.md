# 📦 Comandos Git para Subir tu Proyecto

## 🚀 Pasos para Subir a GitHub

### 1️⃣ Primero: Crea el repositorio en GitHub
1. Ve a https://github.com
2. Click en el **+** (arriba derecha) → **New repository**
3. Nombre: `analisis-numerico-inf133` (o el que prefieras)
4. Descripción: `Aplicación web de métodos numéricos - Flask`
5. **NO marques** "Initialize with README"
6. Click en **Create repository**

---

### 2️⃣ En tu PowerShell (dentro de la carpeta del proyecto):

```powershell
# Verificar que estás en la carpeta correcta
cd "C:\Users\julio\OneDrive\Escritorio\analisis numerico\INF-133\Semana11\web_app_rol_dulceria"

# Inicializar Git
git init

# Agregar todos los archivos
git add .

# Hacer el primer commit
git commit -m "🎉 Initial commit - Aplicación de Análisis Numérico con Flask"

# Cambiar a rama main
git branch -M main

# Conectar con tu repositorio (CAMBIA TU_USUARIO por tu usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/analisis-numerico-inf133.git

# Subir todo
git push -u origin main
```

---

### 3️⃣ Si te pide credenciales:

**Opción A: Personal Access Token (Recomendado)**
1. Ve a GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic)
3. Nombre: `deploy-analisis-numerico`
4. Marca: `repo` (todos los permisos de repositorio)
5. Generate token
6. **COPIA EL TOKEN** (solo se muestra una vez)
7. Usa el token como contraseña cuando Git lo pida

**Opción B: GitHub CLI**
```powershell
# Instalar GitHub CLI
winget install --id GitHub.cli

# Autenticarse
gh auth login

# Seguir instrucciones en pantalla
```

---

## 🔄 Comandos Git Útiles

### Para actualizar cambios después:
```powershell
# Ver qué archivos cambiaron
git status

# Agregar cambios
git add .

# Commit con mensaje
git commit -m "✨ Mejoras en el frontend"

# Subir cambios
git push
```

### Verificar el estado:
```powershell
# Ver commits
git log --oneline

# Ver archivos ignorados
git status --ignored

# Ver ramas
git branch -a
```

### Crear archivo README automático:
```powershell
# Copiar el README que ya tienes
git add README.md
git commit -m "📚 Agregar documentación"
git push
```

---

## 🌐 Después de subir a GitHub

### Para desplegar en Render.com:

1. **Ve a https://render.com**
2. **Sign Up** con tu cuenta de GitHub
3. Click en **New +** → **Web Service**
4. **Connect repository** → Elige `analisis-numerico-inf133`
5. Configuración:
   ```
   Name: analisis-numerico
   Region: Oregon
   Branch: main
   Build Command: pip install -r requirements.txt
   Start Command: cd app && gunicorn run:app --bind 0.0.0.0:$PORT
   Instance Type: Free
   ```
6. Click **Create Web Service**
7. ¡Espera 2-5 minutos y tendrás tu link!

---

## 🎯 Ejemplo Completo de Comandos

```powershell
# 1. Navegar a tu carpeta
cd "C:\Users\julio\OneDrive\Escritorio\analisis numerico\INF-133\Semana11\web_app_rol_dulceria"

# 2. Inicializar Git (solo una vez)
git init

# 3. Agregar archivos
git add .

# 4. Primer commit
git commit -m "🎉 Initial commit - App de Análisis Numérico"

# 5. Crear rama main
git branch -M main

# 6. Conectar con GitHub (CAMBIA TU_USUARIO)
git remote add origin https://github.com/Erickxdps/analisis-numerico-inf133.git

# 7. Subir
git push -u origin main
```

### Si te aparece error de autenticación:
```powershell
# Configurar credenciales (solo primera vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@ejemplo.com"

# Usar token personal cuando pida contraseña
# Usuario: tu_usuario_github
# Password: ghp_XXXXXXXXXXXXXXXXXXXX (el token que generaste)
```

---

## ✅ Verificación Final

Después de `git push`, ve a tu repositorio en GitHub y verifica que veas:
- ✅ Carpeta `app/` con todos los archivos
- ✅ `requirements.txt`
- ✅ `Procfile`
- ✅ `README.md`
- ✅ `.gitignore`
- ✅ `render.yaml`

---

## 🆘 Solución de Problemas Comunes

### Error: "fatal: not a git repository"
```powershell
git init
```

### Error: "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/TU_USUARIO/analisis-numerico-inf133.git
```

### Error: "failed to push some refs"
```powershell
# Forzar push (solo si es tu primer commit)
git push -u origin main --force
```

### Ver logs si hay problemas:
```powershell
git log --oneline --all
git status
git remote -v
```

---

## 🎓 ¡Listo para Desplegar!

Una vez que tu código esté en GitHub, sigue la guía **DEPLOY.md** para tener tu aplicación en línea con un link público. 🚀
