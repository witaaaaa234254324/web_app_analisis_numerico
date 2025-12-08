# 🚀 Guía de Despliegue - Render.com

## Preparación del Proyecto

### 1. Crear archivo `requirements.txt` (ya existe)
```
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
Werkzeug==3.0.1
numpy==1.26.2
scipy==1.11.4
gunicorn==21.2.0
```

### 2. Crear `Procfile` para Render
```
web: cd app && gunicorn run:app
```

### 3. Modificar `run.py` para producción
Agregar al final del archivo:
```python
if __name__ == "__main__":
    # Crea las tablas si no existen
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

## Pasos en Render.com

1. **Crear cuenta en Render.com**
   - Ir a https://render.com
   - Registrarse con GitHub

2. **Conectar repositorio**
   - Subir código a GitHub
   - En Render: New → Web Service
   - Conectar repositorio de GitHub

3. **Configurar el servicio**
   - **Name**: analisis-numerico-app
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `cd app && gunicorn run:app`
   - **Plan**: Free

4. **Variables de entorno** (opcional)
   - `SECRET_KEY`: tu-clave-secreta-super-segura
   - `FLASK_ENV`: production

5. **Deploy**
   - Click en "Create Web Service"
   - Esperar que termine el despliegue
   - Tu app estará en: https://analisis-numerico-app.onrender.com

## 🌐 Alternativas de Despliegue

### PythonAnywhere (Más fácil)

1. Registrarse en https://www.pythonanywhere.com
2. Subir archivos vía "Files" o usar git clone
3. Crear una nueva "Web app" con Flask
4. Configurar WSGI file apuntando a tu aplicación
5. Recargar la web app

### Heroku

1. Instalar Heroku CLI
2. Crear `Procfile`:
   ```
   web: cd app && gunicorn run:app
   ```
3. Comandos:
   ```bash
   heroku login
   heroku create analisis-numerico
   git push heroku main
   ```

### Railway.app

1. Conectar repositorio de GitHub
2. Railway detecta automáticamente Flask
3. Deploy automático

## ⚙️ Consideraciones para Producción

### Seguridad
- Cambiar `SECRET_KEY` por variable de entorno
- Deshabilitar `DEBUG = False`
- Usar HTTPS

### Base de Datos
- Para producción, considera PostgreSQL:
  ```python
  import os
  app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///analisis_numerico.db")
  ```

### Rendimiento
- Usar un servidor WSGI como Gunicorn
- Considerar cache (Flask-Caching)
- Optimizar consultas a BD

## 📋 Checklist Pre-Deploy

- [ ] Archivo `requirements.txt` actualizado
- [ ] `Procfile` creado
- [ ] Variables de entorno configuradas
- [ ] DEBUG = False en producción
- [ ] SECRET_KEY seguro
- [ ] Base de datos inicializada
- [ ] Probado localmente
- [ ] Código subido a GitHub

## 🧪 Probar Localmente Antes de Deploy

```powershell
# Instalar gunicorn
pip install gunicorn

# Probar con gunicorn localmente
cd app
gunicorn run:app --bind 0.0.0.0:5000
```

Abrir http://localhost:5000 y verificar que funcione correctamente.

## 📱 Usuarios de Prueba

Asegúrate de crear usuarios de prueba para la demo:

```python
# En producción, ejecutar una vez:
from run import app, db
from models.user_model import User

with app.app_context():
    db.create_all()
    admin = User("Admin", "Demo", "admin", "admin2025", role="admin")
    admin.save()
    user = User("Usuario", "Prueba", "demo", "demo2025", role="user")
    user.save()
```

## 🎯 URLs de Ejemplo

Después del deploy, tendrás acceso a:
- **Login**: https://tu-app.onrender.com/login
- **Métodos**: https://tu-app.onrender.com/metodos
- **CG**: https://tu-app.onrender.com/gradiente-conjugado
- **SOR**: https://tu-app.onrender.com/sor
- **Raíces**: https://tu-app.onrender.com/raices
- **Interpolación**: https://tu-app.onrender.com/interpolacion

---

**¡Tu aplicación estará lista para presentar!** 🎉
