from django.contrib import admin
from .models import Cliente, Membresia, Pago

# El uso de decoradores (@admin.register) es una forma moderna de registras modelos.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # list_display: Qué columnas se ven en la tabla
    list_display = ('nombre', 'telefono', 'email', 'edad', 'fecha_registro')
    
    # search_fields: Crea una barra de busqueda. Busca por nombre, teléfono o email
    search_fields = ('nombre', 'telefono', 'email')
    
    # list_filter: Crea un panel lateal para filtrar
    list_filter = ('fecha_registro',)
    
    # ordering: Ordena por defecto en el admin
    ordering = ('-fecha_registro',)
    
@admin.register(Membresia)
class MembresiaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'tipo', 'costo', 'fecha_inicio', 'fecha_termino', 'estado_visual')
    list_filter = ('tipo', 'activa', 'fecha_inicio')
    search_fields = ('cliente__nombre', 'cliente__email') # la busqueda se realiza dentro de la relación Cliente
    autocomplete_fields = ['cliente'] # esto crea un buscador en lugar de una lista
    
    # metodo personalizado para mostrar un icono visual en lugar de "True/False"
    def estado_visual(self, obj):
        if obj.activa:
            return "✅ Activa"
        return "❌ Vencida"
    estado_visual.short_description = "Estado"
    
@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'monto', 'fecha_pago', 'comentario_corto')
    list_filter = ('fecha_pago',)
    search_fields = ('cliente__nombre',)
    
    # Mostramos solo los primeros 50 caracteres del comentario para no romper la tabla
    def comentario_corto(self, obj):
        return obj.comentario[:50] + "..." if obj.comentario else "-"
    comentario_corto.short_description = "Notas"
    
    