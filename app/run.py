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

if __name__ == "__main__":
    # Crea las tablas si no existen
    with app.app_context():
        db.create_all()
    # Configuración para desarrollo/producción
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") != "production"
    app.run(debug=debug, host='0.0.0.0', port=port)

if __name__ == "__main__":
    # Crea las tablas si no existen
    with app.app_context():
        db.create_all()
    app.run(debug=True)
