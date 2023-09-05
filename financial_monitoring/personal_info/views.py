from rest_framework.views import APIView
from rest_framework.response import Response
from personal_data.models import PersonalData
from personal_data.serializers import PersonalDataSerializer
from family_composition.models import FamilyComposition
from family_composition.serializers import FamilyCompositionSerializer
from education.models import Education
from education.serializers import EducationSerializer
from owning_languages.models import OwningLanguages
from owning_languages.serializers import OwningLanguagesSerializer
from academic_degree.models import AcademicDegree
from academic_degree.serializers import AcademicDegreeSerializer
from sport_results.models import SportResults
from sport_results.serializers import SportResultSerializers
from general_info.models import GeneralInfo
from courses.models import Courses
from courses.serializers import CoursesSerializer
from rest_framework import status


class PersonalInfoAPIView(APIView):
    available_models = {'personal_data': PersonalData,
                        'family_compositions': FamilyComposition,
                        'educations': Education,
                        'owning_languages': OwningLanguages,
                        'courses' : Courses,
                        'academic_degree': AcademicDegree,
                        'sport_results': SportResults
                        }

    available_serializers = {
        'personal_data': PersonalDataSerializer,
        'family_compositions': FamilyCompositionSerializer,
        'educations': EducationSerializer,
        'owning_languages': OwningLanguagesSerializer,
        'courses': CoursesSerializer,
        'academic_degree': AcademicDegreeSerializer,
        'sport_results': SportResultSerializers,
    }

    def get(self, request, id, format=None):

        if id is None:
            return Response({'message': 'Введите корректный ID'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            general_info = GeneralInfo.objects.get(id=id)
        except:
            return Response({'message': 'Пользователь с таким ID не найден'}, status=status.HTTP_404_NOT_FOUND)

        response_data = {}

        for related_name, serializer in self.available_serializers.items():
            related_queryset = getattr(general_info, related_name).all()
            if related_name != 'personal_data':
                response_data[related_name] = serializer(related_queryset, many=True).data
            else:
                if (len(related_queryset)) >= 1:
                    response_data[related_name] = serializer(related_queryset[0]).data
                else:
                    response_data[related_name] = {}
    
        return Response(response_data, status=status.HTTP_200_OK)

    def patch(self, request, format=None):
        fields_list = request.data.keys()

        for model_name in fields_list:
            if model_name not in self.available_models.keys():
                print(f"model {model_name} is here")
                continue
            
            current_data = request.data.get(model_name)

            if model_name == 'personal_data':
                current_data = [current_data]

            for data in current_data:
                id = data.pop('id', None)

                if id:
                    self.available_models[model_name].objects.filter(
                        id=id).update(**data)

        return Response({"message": "Object updated successfully"}, status=200)

    # def delete(self, request, iin, format=None):
    #
    #     if iin is None:
    #         return Response({'message': 'Введите корректный ИИН'})
    #
    #     for model in self.available_models.values():
    #         queryset = model.objects.filter(iin=iin)
    #         queryset.delete()
    #
    #     return Response({"message": "Object deleted successfully"}, status=200)

    def post(self, request, *args, **kwargs):
        fields_list = request.data.keys()

        response = {model_name: []
                    for model_name in self.available_models.keys()}

        for model_name in fields_list:
            if model_name not in self.available_models.keys():
                continue

            current_data = request.data.get(model_name)

            if model_name == 'personal_data':
                current_data = [current_data]

            for data in current_data:
                id = data.get('iin', None)

                if not id:
                    continue
                
                try:
                    general_info = GeneralInfo.objects.get(id=id)
                except:
                    print('General info with id {} not found'.format(id))
                    continue

                serializer = self.available_serializers[model_name](data=data)
                if serializer.is_valid():
                    serializer_data = serializer.data
                    serializer_data['iin'] = general_info
                    self.available_models[model_name].objects.create(**serializer_data)
                    response_data = serializer.data
                    response_data['iin'] = general_info.id
                    response[model_name].append(response_data)
                else:
                    print(serializer.errors)

        return Response(response, status=201)
