from django.shortcuts import render
from .models import Cliente

def lista_clientes(request):
    # comenzamos consultando la base de datos (select * from Cliente)
    clientes = Cliente.objects.all()
    
    # Enviamos los datos al html
    return render(request, 'core/lista_clientes.html', {'clientes': clientes})

