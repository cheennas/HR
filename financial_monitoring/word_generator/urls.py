from django.urls import path
from .views import GenerateDocumentView


urlpatterns = [
    path('generate-document/<int:id>', GenerateDocumentView.as_view(), name='generate_document'),
]