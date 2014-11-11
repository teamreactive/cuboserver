from django.db import models


class Cliente(models.Model):
	nit = models.CharField(max_length=25, unique=True)
	verificacion = models.CharField(max_length=25, null=True, blank=True, unique=True)
	razon = models.CharField(max_length=25, unique=True)
	sigla = models.CharField(max_length=10, null=True, blank=True)
	logo = models.ImageField(upload_to="logos", null=True, blank=True)

	def save(self, *args, **kwargs):
		self.id = Cliente.objects.all().order_by("-id")[0].id + 1
		super(Cliente, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.nit)

	class Meta:
		db_table = "cliente"
