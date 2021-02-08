from rest_framework.exceptions import APIException, ValidationError
# from rest_framework.views import exception_handler


class APIError(APIException):
  default_detail = 'Erro interno. Entre em contato com nosso suporte.'
  default_code = 'api_error'

  def __init__(self, custom_detail=None, status_code=None, *args, **kwargs):
    detail = {'detail': custom_detail or self.default_detail}
    self.status_code = status_code or self.status_code
    super().__init__(detail)


class ExternalServiceError(APIException):
  status_code = 502
  default_detail = 'Erro em serviço externo. Entre em contato com nosso suporte.'
  default_code = 'external_service_error'


class BaseValidationError(APIError):
  default_detail = 'Erro interno de validação de dados. Entre em contato com nosso suporte.'
  status_code = 400

