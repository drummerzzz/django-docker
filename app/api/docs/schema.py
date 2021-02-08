from rest_framework.permissions import IsAdminUser
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
  openapi.Info(
    title="Viralize API",
    default_version='v1',
    description="Plataforma de compra de publicações para Instagram, Facebook e Linkedin",
    terms_of_service="https://app.viralize.online/termos-de-servico/",
    contact=openapi.Contact(email="agencia@viralize.online"),
    license=openapi.License(name="Copyright License"),
  ),
  public=False,
  permission_classes=[IsAdminUser]
)
