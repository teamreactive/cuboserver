from django.db import models
from django.utils.six import with_metaclass

from unidecode import unidecode

class UpperCharField(with_metaclass(models.SubfieldBase, models.CharField)):
	def __init__(self, *args, **kwargs):
		self.is_uppercase = kwargs.pop('uppercase', True)
		super(UpperCharField, self).__init__(*args, **kwargs)

	def get_prep_value(self, value):
		value = super(UpperCharField, self).get_prep_value(value)
		if value and self.is_uppercase:
			return unidecode(value).upper()

		return value