from django.urls import path
from .views import GenerateDocumentView


urlpatterns = [
    path('generate-document/<str:iin>', GenerateDocumentView.as_view(), name='generate_document'),
]