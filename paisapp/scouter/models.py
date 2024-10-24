from django.db import models

# Create your models here.
class Scout(models.Model):
	name = models.CharField(max_length=255)
	img = models.ImageField(upload_to='scouts/')
	latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
	longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	