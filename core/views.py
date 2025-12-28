from django.shortcuts import render
from django.contrib.auth.decorators import login_required # con eso se importa un candado de seguridad
from .models import Cliente
from django.http import HttpResponse
from django.contrib.auth.models import User

@login_required
def lista_clientes(request):
    # comenzamos consultando la base de datos (select * from Cliente)
    clientes = Cliente.objects.all()
    
    # Enviamos los datos al html
    return render(request, 'core/lista_clientes.html', {'clientes': clientes})

def crear_admin_rapido(request):
    # Verificamos si ya existe para no crear duplicados
    if not User.objects.filter(username='admin').exists():
        # Crea el usuario: admin / correo@ejemplo.com / clave: admin123
        User.objects.create_superuser('admin', 'admin@ejemplo.com', 'admin123')
        return HttpResponse("¡Listo! Superusuario 'admin' creado con clave 'admin123'.")
    else:
        return HttpResponse("El usuario 'admin' ya existe. Intenta loguearte.")

