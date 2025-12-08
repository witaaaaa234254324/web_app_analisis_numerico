# Script de Inicialización de la Aplicación
# Ejecuta este script para configurar la base de datos por primera vez

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Inicializando Aplicación de Análisis Numérico" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si existe un entorno virtual
if (-not (Test-Path "venv")) {
    Write-Host "Creando entorno virtual..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "Entorno virtual creado." -ForegroundColor Green
}

# Activar entorno virtual
Write-Host "Activando entorno virtual..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Instalar dependencias
Write-Host "Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt

# Cambiar al directorio de la aplicación
Set-Location app

# Inicializar base de datos
Write-Host ""
Write-Host "Inicializando base de datos..." -ForegroundColor Yellow

$initScript = @"
from run import app, db
from models.user_model import User

with app.app_context():
    db.create_all()
    
    # Verificar si ya existen usuarios
    existing_admin = User.get_user_by_username('admin')
    if not existing_admin:
        admin = User('Admin', 'Sistema', 'admin', 'admin123', role='admin')
        admin.save()
        print('✓ Usuario administrador creado: admin / admin123')
    else:
        print('⚠ Usuario administrador ya existe')
    
    existing_user = User.get_user_by_username('user')
    if not existing_user:
        user = User('Usuario', 'Demo', 'user', 'user123', role='user')
        user.save()
        print('✓ Usuario demo creado: user / user123')
    else:
        print('⚠ Usuario demo ya existe')
    
    print('\n✓ Base de datos inicializada correctamente')
"@

python -c $initScript

# Volver al directorio raíz
Set-Location ..

Write-Host ""
Write-Host "==================================" -ForegroundColor Green
Write-Host "Inicialización completada" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Green
Write-Host ""
Write-Host "Para iniciar la aplicación, ejecuta:" -ForegroundColor Yellow
Write-Host "  cd app" -ForegroundColor Cyan
Write-Host "  python run.py" -ForegroundColor Cyan
Write-Host ""
Write-Host "Usuarios por defecto:" -ForegroundColor Yellow
Write-Host "  Admin: admin / admin123" -ForegroundColor Cyan
Write-Host "  Usuario: user / user123" -ForegroundColor Cyan
Write-Host ""
Write-Host "La aplicación estará disponible en:" -ForegroundColor Yellow
Write-Host "  http://127.0.0.1:5000" -ForegroundColor Cyan
Write-Host ""
