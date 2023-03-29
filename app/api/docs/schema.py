from rest_framework.permissions import IsAdminUser
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
  openapi.Info(
    title="Title",
    default_version='v1',
    description="Description",
    terms_of_service="/termos-de-servico/",
    contact=openapi.Contact(email="admin@mail.com"),
    license=openapi.License(name="Copyright License"),
  ),
  public=False,
  permission_classes=[IsAdminUser]
)
