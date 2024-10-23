from django.db import models

# Create your models here.
class Categoria(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Tipo(models.Model):
	name = models.CharField(max_length=100)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)

	def __str__(self):
		return self.name