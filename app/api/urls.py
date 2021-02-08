from django.urls import path, include


urlpatterns = [
  path('', include('app.api.docs.urls'))
]
