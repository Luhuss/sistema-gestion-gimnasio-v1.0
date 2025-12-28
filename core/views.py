from django.shortcuts import render
from django.contrib.auth.decorators import login_required # con eso se importa un candado de seguridad
from .models import Cliente

@login_required
def lista_clientes(request):
    # comenzamos consultando la base de datos (select * from Cliente)
    clientes = Cliente.objects.all()
    
    # Enviamos los datos al html
    return render(request, 'core/lista_clientes.html', {'clientes': clientes})


