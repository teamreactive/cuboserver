from django.db import models

class Contacto(models.Model):
	nombre = models.CharField(max_length=25)
	apellido = models.CharField(max_length=25)
	telefono = models.CharField(max_length=15, null=True, blank=True)
	extension = models.CharField(max_length=5, null=True, blank=True)
	celular = models.CharField(max_length=15, null=True, blank=True)
	email = models.EmailField(max_length=25, null=True, blank=True)
	cargo = models.CharField(max_length=25, null=True, blank=True)
	perfil = models.TextField(null=True, blank=True)

	def save(self, *args, **kwargs):
		if self.id is None:
			self.id = 1
			try: self.id = Contacto.objects.all().order_by("-id")[0].id + 1
			except: pass
		super(Contacto, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.nombre)

	class Meta:
		db_table = "contacto"
