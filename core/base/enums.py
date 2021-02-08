from django.db.models import TextChoices, IntegerChoices
from django.utils.translation import gettext_lazy as _

class TypeOfPersonChoice(TextChoices):
  FISICA = 'f', _('Física')
  JURIDICA = 'j', _('Jurídica')


class TypeOfCompanyChoice(IntegerChoices):
  INFORMAL = 0, _('Informal')
  MEI = 1, _('MEI')
  INDIVIDUAL = 2, _('Individual')
  EIRELI = 3, _('Eireli')
  LTDA = 4, _('LTDA')