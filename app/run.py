from flask import Flask
from flask_login import LoginManager
import os

# Importamos los controladores
from controllers import user_controller
from controllers import method_controller

# Importamos la base de datos
from database import db
from models.user_model import User

# Inicializa la aplicación Flask
app = Flask(__name__)
# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///analisis_numerico.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "clave-secreta-analisis-numerico-2025")
# Configuración de Flask-Login
login_manager = LoginManager()
# Especifica la ruta de inicio de sesión
login_manager.login_view = "user.login"
login_manager.init_app(app)


# Función para cargar un usuario basado en su ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Inicializa `db` con la aplicación Flask
db.init_app(app)
# Registra los Blueprints
app.register_blueprint(user_controller.user_bp)
app.register_blueprint(method_controller.method_bp)


def init_database_and_users():
    """Inicializa la base de datos y crea usuarios por defecto si no existen"""
    with app.app_context():
        # Crear tablas
        db.create_all()
        
        # Verificar si ya existen usuarios
        existing_users = User.query.count()
        
        if existing_users == 0:
            print("🔧 Creando usuarios por defecto...")
            
            # Crear usuario administrador
            admin = User(
                name="Admin",
                last_name="Sistema",
                username="admin",
                password="admin123",
                role="admin"
            )
            admin.save()
            print(f"✅ Usuario admin creado: admin / admin123")
            
            # Crear usuario demo
            demo_user = User(
                name="Usuario",
                last_name="Demo",
                username="user",
                password="user123",
                role="user"
            )
            demo_user.save()
            print(f"✅ Usuario demo creado: user / user123")
            
            print("🎉 Base de datos inicializada con usuarios por defecto")
        else:
            print(f"ℹ️  Base de datos ya tiene {existing_users} usuario(s)")


# IMPORTANTE: Inicializar la BD cuando la app se carga (para producción con gunicorn)
# Esto se ejecuta SIEMPRE, incluso cuando gunicorn importa el módulo
try:
    init_database_and_users()
except Exception as e:
    print(f"⚠️  Error al inicializar base de datos: {e}")
    # Intentar al menos crear las tablas
    with app.app_context():
        db.create_all()
        print("✅ Tablas creadas (sin usuarios por defecto)")


if __name__ == "__main__":
    # Este bloque solo se ejecuta en desarrollo (python run.py)
    # En producción con gunicorn, no se ejecuta
    
    # Configuración para desarrollo/producción
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") != "production"
    app.run(debug=debug, host='0.0.0.0', port=port)
