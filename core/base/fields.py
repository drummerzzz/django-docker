from django.db.models import CharField
from core.base.validators import (
  validate_cpf, validate_cnpj,
  validate_cpf_cnpj, validate_zip_code
)


class ZipCodeField(CharField):

  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = 9
    kwargs['validators'] = [validate_zip_code]
    super().__init__(*args, **kwargs)



class CpfField(CharField):

  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = 14
    kwargs['validators'] = [validate_cpf]
    super().__init__(*args, **kwargs)



class CnpjField(CharField):
  
  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = 18
    kwargs['validators'] = [validate_cnpj]
    super().__init__(*args, **kwargs)


class CpfCnpjField(CharField):
  
  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = 18
    kwargs['validators'] = [validate_cpf_cnpj]
    super().__init__(*args, **kwargs)