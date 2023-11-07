from django.db import models

# Create your models here.
class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "provincias"
        db_table = "provincia"

    def __str__(self):
        return self.nombre
    

class Agenda(models.Model):
    DNI = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fec_nac = models.DateField()
    domicilio = models.CharField( max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='agenda', null=True)

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "agendas"
        db_table = "agenda"

    def __str__(self):
        return self.nombre