from rest_framework.views import APIView
from rest_framework.response import Response

from spec_check.models import SpecCheck
from attestation.models import Attestation
from awards.models import Awards
from investigation_retrieval.models import InvestigationRetrieval
from class_category.models import ClassCategory
from autobiography.models import Autobiography
from sick_leaves.models import SickLeaves

from spec_check.serializers import SpecCheckSerializer
from attestation.serializers import AttestationSerializer
from awards.serializers import AwardsSerializer
from investigation_retrieval.serializers import InvestigationRetrievalSerializer
from class_category.serializers import ClassCategorySerializer
from autobiography.serializers import AutobiographySerializer
from sick_leaves.serializers import SickLeavesSerializer

from rest_framework import status
from general_info.models import GeneralInfo


class StaffInfoAPIView(APIView):

    available_models = {'spec_checks': SpecCheck,
                        'attestations': Attestation,
                        'awards': Awards,
                        'investigation_retrievals': InvestigationRetrieval,
                        'class_categories': ClassCategory,
                        'autobiography': Autobiography,
                        'sick_leaves': SickLeaves,
                        }

    available_serializers = {'spec_checks': SpecCheckSerializer,
                             'attestations': AttestationSerializer,
                             'awards': AwardsSerializer,
                             'investigation_retrievals': InvestigationRetrievalSerializer,
                             'class_categories': ClassCategorySerializer,
                             'autobiography': AutobiographySerializer,
                             'sick_leaves': SickLeavesSerializer,
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
            if related_name != 'autobiography':
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
                continue

            current_data = request.data.get(model_name)

            if model_name == 'autobiography':
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



            if model_name == 'autobiography':
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
