from django.db import models

class Persona(models.Model):
	nombre=models.CharField(max_length=255)
	apodo=models.CharField(max_length=255, blank=True)
	foto=models.ImageField(upload_to='personas')
	limiteCredito=models.PositiveIntegerField()
	obs=models.TextField(blank=True)

	def __unicode__(self):
		return self.nombre
		