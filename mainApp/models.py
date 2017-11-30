from django.db import models

# Create your models here.
class CotizaOficinas(models.Model):
    id_oficina = models.AutoField(primary_key=True)
    cve_corta = models.CharField(max_length=6)
    razon_social = models.CharField(max_length=60)
    consecutivo = models.DecimalField(max_digits=12, decimal_places=0)
    observaciones = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cotiza_oficinas'
