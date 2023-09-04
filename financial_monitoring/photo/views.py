from .serializers import PhotoSerializer
from .models import Photo
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import os
from django.conf import settings


class PhotoView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        general_info_id = request.query_params.get('general_info_id')

        if general_info_id is None:
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(iin__id=general_info_id)

        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PhotoSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            photo = Photo.objects.get(pk=pk)
            print(str(photo.photo))
            file_path = os.path.join(settings.MEDIA_ROOT, str(photo.photo))

            if os.path.exists(file_path):
                os.remove(file_path)

            photo.delete()
            return Response({"detail": f"Photo with id {pk} was deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Photo.DoesNotExist:
            return Response({"detail": "Photo not found"}, status=status.HTTP_404_NOT_FOUND)