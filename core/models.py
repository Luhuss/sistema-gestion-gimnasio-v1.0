from django.db import models
from django.utils import timezone

#1 clase cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre Completo")
    edad = models.PositiveBigIntegerField(verbose_name="Edad") # Positive evita números negativos
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.EmailField(blank=True, null=True, verbose_name="Correo Electrónico")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-fecha_registro'] # ordena del más nuevo al más antiguo
        
    def __str__(self):
        return f"{self.nombre} | {self.telefono}"
    
class Membresia(models.Model):
    TIPOS = [
        ('MENSUAL', 'Plan Mensual'),
        ('TRIMESTRAL', 'Plan Trimestral'),
        ('ANUAL', 'Plan Anual'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='membresias', verbose_name="Cliente")
    tipo = models.CharField(max_length=15, choices=TIPOS, verbose_name="Tipo de Plan")
    costo = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Costo ($)") # 0 decimales para $ chilenos
    fecha_inicio = models.DateField(default=timezone.now, verbose_name="Fecha de Inicio")
    fecha_termino = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de Término")
    activa = models.BooleanField(default=True, verbose_name="¿Está activa?")
    
    class Meta:
        verbose_name = "Membresía"
        verbose_name_plural = "Membresías"
        
    def __str__(self):
        estado = "ACTIVA" if self.activa else "VENCIDA"
        return f"{self.get_tipo_display()} - {self.cliente.nombre} ({estado})"
    
class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, verbose_name="Cliente")
    monto = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Monto Pagado")
    fecha_pago = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora")
    comentario = models.TextField(blank=True, null=True, verbose_name="Notas Adicionales")
    
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Historial de Pagos"
        ordering = ['-fecha_pago']
        
    def __str__(self):
        return f"${self.monto} - {self.cliente}"
            
