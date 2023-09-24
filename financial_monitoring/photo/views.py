from .serializers import PhotoSerializer
from .models import Photo
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import base64
from general_info.models import GeneralInfo
import os
from django.conf import settings


class PhotoView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # def get(self, request, *args, **kwargs):
    #     general_info_id = request.query_params.get('general_info_id')
    #
    #     if general_info_id is None:
    #         photos = Photo.objects.all()
    #     else:
    #         photos = Photo.objects.filter(iin__id=general_info_id)
    #
    #     serializer = PhotoSerializer(photos, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, *args, **kwargs):
    #     posts_serializer = PhotoSerializer(data=request.data)
    #     if posts_serializer.is_valid():
    #         posts_serializer.save()
    #         return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         print('error', posts_serializer.errors)
    #         return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, *args, **kwargs):
    #     try:
    #         photo = Photo.objects.get(pk=pk)
    #         print(str(photo.photo))
    #         file_path = os.path.join(settings.MEDIA_ROOT, str(photo.photo))
    #
    #         if os.path.exists(file_path):
    #             os.remove(file_path)
    #
    #         photo.delete()
    #         return Response({"detail": f"Photo with id {pk} was deleted"}, status=status.HTTP_204_NO_CONTENT)
    #     except Photo.DoesNotExist:
    #         return Response({"detail": "Photo not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        image_data = request.FILES.get('photo')
        general_info_id = request.data.get('iin')

        if image_data and general_info_id:
            try:
                # Read the content of the uploaded image file
                image_bytes = image_data.read()

                # Encode the image data to base64
                image_data_base64 = base64.b64encode(image_bytes).decode('utf-8')
                # print(f"image data base64 :{image_data_base64}")
                # Find the associated GeneralInfo object
                general_info = GeneralInfo.objects.get(pk=general_info_id)
                # print(f"{general_info} : general info")

                # Create and save the Photo object
                photo = Photo(iin=general_info, photo=image_data_base64)
                # print(photo)
                photo.save()

                return Response({'message': 'Image saved successfully'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'message': 'Error saving image', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Invalid data received'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        try:
            general_info = GeneralInfo.objects.get(pk=id)
            photos = Photo.objects.filter(iin=general_info)

            # Serialize the photos
            serializer = PhotoSerializer(photos, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except GeneralInfo.DoesNotExist:
            return Response({'message': 'GeneralInfo not found'}, status=status.HTTP_404_NOT_FOUND)


class PhotoDeleteView(APIView):

    def delete(self, request, photo_id):
        try:
            photo = Photo.objects.get(pk=photo_id)
            photo.delete()
            return Response({"detail": f"Photo with id {photo_id} was deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Photo.DoesNotExist:
            return Response({"detail": "Photo not found"}, status=status.HTTP_404_NOT_FOUND)
