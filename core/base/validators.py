# import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from validate_docbr import CPF, CNPJ

from core.base.utils import clean_special_characters

def validate_cpf(value):
  value = clean_special_characters(value)
  doc = CPF()
  if doc.validate(value):
    raise ValidationError(
      _('%(value)s is not an %(doc_type) valid'),
      params={'value': value, 'doc_type': 'CPF'},
    )

def validate_cnpj(value):
  value = clean_special_characters(value)
  doc = CNPJ() 
  if doc.validate(value):
    raise ValidationError(
      _('%(value)s is not an %(doc_type) valid'),
      params={'value': value, 'doc_type': 'CNPJ'},
    )

def validate_cpf_cnpj(value):
  value = clean_special_characters(value)
  if len(value) > 11:
    return validate_cnpj(value)
  return validate_cpf(value)


def validate_zip_code(value):
  value = clean_special_characters(value)
  if len(value) != 8:
    raise ValidationError(
      _('%(value)s is not an zip code valid'),
      params={'value': value},
    )
    