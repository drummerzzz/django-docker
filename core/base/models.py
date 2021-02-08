from django.db import models
from django.utils.translation import gettext_lazy as _

from core.base.validators import validate_zip_code, validate_cpf_cnpj
from core.base.enums import TypeOfPersonChoice
from core.base.fields import CnpjField, ZipCodeField, CpfCnpjField

class AddressMixin(models.Model):
  
  street = models.CharField(max_length=120)
  street_number = models.CharField(max_length=50)
  district = models.CharField(max_length=80)
  city = models.CharField(max_length=80)
  state = models.CharField(max_length=2)
  complement = models.CharField(max_length=250, blank=True)
  zip_code = ZipCodeField()

  class Meta:
    abstract = True


class PhoneMixin(models.Model):

  phone_prefix = models.CharField(max_length=2)
  phone_number = models.CharField(max_length=9)
    
  def phone(self):
    return f'({self.phone_prefix} {self.phone_number}'

  class Meta:
      abstract = True


class PersonDocumentMixin(models.Model):

  type_person = models.CharField(
    _("Tipo de pessoa"),
    max_length=5,
    choices=TypeOfPersonChoice.choices,
    default=TypeOfPersonChoice.FISICA
  )
  cpf_cnpj = CnpjField()
  
  class Meta:
    abstract = True

