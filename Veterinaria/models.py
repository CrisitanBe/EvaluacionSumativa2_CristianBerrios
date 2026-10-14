from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre= models.CharField(max_length=50, unique= True)
    mascota= models.CharField(max_length=15, unique= True)
    Sintomas= models.CharField(max_length=200, unique= True)
    Prioridad= models.BooleanField(default=False)


    def __str__(self):
        return self.nombre







class Atencion(models.Model):
    pabellon= models.CharField(max_length=1, unique= False,default="A")
    asistencia= models.BooleanField()
    costo=models.PositiveIntegerField()
    Diagnosticoprevio= models.CharField(max_length=200, unique= True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='Atencion',
    )
    def __str__(self):
        return self.pabellon
    





