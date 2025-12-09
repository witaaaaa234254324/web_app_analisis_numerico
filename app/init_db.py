"""
Script para inicializar la base de datos con usuarios por defecto
Útil para producción o cuando necesites resetear la BD
"""
from run import app, db
from models.user_model import User

def init_database():
    """Inicializa la base de datos y crea usuarios por defecto"""
    with app.app_context():
        print("🔧 Creando tablas...")
        db.create_all()
        print("✅ Tablas creadas")
        
        # Verificar si ya existen usuarios
        existing_users = User.query.all()
        
        if len(existing_users) > 0:
            print(f"\n⚠️  La base de datos ya tiene {len(existing_users)} usuario(s):")
            for user in existing_users:
                print(f"   - {user.username} ({user.role})")
            
            respuesta = input("\n¿Deseas agregar usuarios de todas formas? (s/n): ")
            if respuesta.lower() != 's':
                print("❌ Operación cancelada")
                return
        
        print("\n🔧 Creando usuarios por defecto...")
        
        # Crear usuario administrador si no existe
        admin_exists = User.query.filter_by(username="admin").first()
        if not admin_exists:
            admin = User(
                name="Admin",
                last_name="Sistema",
                username="admin",
                password="admin123",
                role="admin"
            )
            admin.save()
            print(f"✅ Usuario admin creado")
            print(f"   Usuario: admin")
            print(f"   Contraseña: admin123")
            print(f"   Rol: Administrador")
        else:
            print(f"ℹ️  Usuario 'admin' ya existe")
        
        # Crear usuario demo si no existe
        user_exists = User.query.filter_by(username="user").first()
        if not user_exists:
            demo_user = User(
                name="Usuario",
                last_name="Demo",
                username="user",
                password="user123",
                role="user"
            )
            demo_user.save()
            print(f"\n✅ Usuario demo creado")
            print(f"   Usuario: user")
            print(f"   Contraseña: user123")
            print(f"   Rol: Usuario normal")
        else:
            print(f"ℹ️  Usuario 'user' ya existe")
        
        print("\n" + "="*50)
        print("🎉 Base de datos inicializada correctamente")
        print("="*50)
        print("\n📝 USUARIOS DISPONIBLES:")
        print("   1. admin / admin123 (Administrador)")
        print("   2. user / user123 (Usuario normal)")
        print("\n💡 Puedes usar estos usuarios para iniciar sesión")


if __name__ == "__main__":
    print("="*50)
    print("Inicialización de Base de Datos")
    print("Aplicación: Análisis Numérico")
    print("="*50)
    init_database()
