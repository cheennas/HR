from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from general_info.models import GeneralInfo
from academic_degree.models import AcademicDegree
from attestation.models import Attestation
from autobiography.models import Autobiography
from awards.models import Awards
from class_category.models import ClassCategory
from courses.models import Courses
from education.models import Education
from family_composition.models import FamilyComposition
from investigation_retrieval.models import InvestigationRetrieval
from military_rank.models import MilitaryRank
from orders_list.models import OrdersList
from owning_languages.models import OwningLanguages
from personal_data.models import PersonalData
from photo.models import Photo
from sick_leaves.models import SickLeaves
from spec_check.models import SpecCheck
from sport_results.models import SportResults
from working_history.models import WorkingHistory

from general_info.serializers import GeneralInfoSerializer
from academic_degree.serializers import AcademicDegreeSerializer
from attestation.serializers import AttestationSerializer
from autobiography.serializers import AutobiographySerializer
from awards.serializers import AwardsSerializer
from class_category.serializers import ClassCategorySerializer
from courses.serializers import CoursesSerializer
from education.serializers import EducationSerializer
from family_composition.serializers import FamilyCompositionSerializer
from investigation_retrieval.serializers import InvestigationRetrievalSerializer
from military_rank.serializers import MilitaryRankSerializer
from orders_list.serializers import OrdersListSerializer
from owning_languages.serializers import OwningLanguagesSerializer
from personal_data.serializers import PersonalDataSerializer
from photo.serializers import PhotoSerializer
from sick_leaves.serializers import SickLeavesSerializer
from spec_check.serializers import SpecCheckSerializer
from sport_results.serializers import SportResultSerializers
from working_history.serializers import WorkingHistorySerializer


class StaffMainView(APIView):
    available_models = {'general_info': GeneralInfo,
                        'personal_data': PersonalData,
                        'family_compositions': FamilyComposition,
                        'educations': Education,
                        'owning_languages': OwningLanguages,
                        'academic_degree': AcademicDegree,
                        'sport_results': SportResults,
                        'spec_checks': SpecCheck,
                        'attestations': Attestation,
                        'awards': Awards,
                        'photo': Photo,
                        'courses': Courses,
                        'military_rank': MilitaryRank,
                        'orders_list': OrdersList,
                        'investigation_retrievals': InvestigationRetrieval,
                        'class_categories': ClassCategory,
                        'autobiography': Autobiography,
                        'sick_leaves': SickLeaves,
                        'working_histories': WorkingHistory,
                        }

    available_serializers = {'general_info': GeneralInfoSerializer,
                             'personal_data': PersonalDataSerializer,
                             'family_compositions': FamilyCompositionSerializer,
                             'educations': EducationSerializer,
                             'owning_languages': OwningLanguagesSerializer,
                             'academic_degree': AcademicDegreeSerializer,
                             'sport_results': SportResultSerializers,
                             'spec_checks': SpecCheckSerializer,
                             'attestations': AttestationSerializer,
                             'awards': AwardsSerializer,
                             'photo': PhotoSerializer,
                             'courses': CoursesSerializer,
                             'military_rank': MilitaryRankSerializer,
                             'orders_list': OrdersListSerializer,
                             'investigation_retrievals': InvestigationRetrievalSerializer,
                             'class_categories': ClassCategorySerializer,
                             'autobiography': AutobiographySerializer,
                             'sick_leaves': SickLeavesSerializer,
                             'working_histories': WorkingHistorySerializer,
                             }

    def post(self, request, *args, **kwargs):
        fields_list = request.data.keys()

        response = {model_name: []
                    for model_name in self.available_models.keys()}

        # CREATING GENERAL INFO INSTANCE
        general_info_data = request.data.get('general_info')

        if general_info_data is None:
            return Response({"detail": "General Info data not found"}, status=status.HTTP_404_NOT_FOUND)

        general_info_serializer = self.available_serializers['general_info'](data=general_info_data)

        if general_info_serializer.is_valid():
            general_info = self.available_models['general_info'].objects.create(**general_info_serializer.data)

        # CREATING OTHER MODELS INSTANCES
        for model_name in fields_list:
            if model_name not in self.available_models.keys() or model_name == 'general_info':
                continue

            current_data = request.data.get(model_name)

            if model_name == 'personal_data' or model_name == 'autobiography' or model_name == 'photo' or model_name == 'military_rank':
                current_data = [current_data]

            for data in current_data:
                data['iin'] = general_info.id

                serializer = self.available_serializers[model_name](data=data)

                if serializer.is_valid():
                    serializer_data = serializer.data
                    serializer_data['iin'] = general_info
                    self.available_models[model_name].objects.create(**serializer_data)
                    response_data = serializer.data
                    response_data['iin'] = general_info.id
                    response[model_name].append(serializer.data)
                else:
                    print(serializer.errors)

        return Response(response, status=201)
