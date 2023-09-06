from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.db import connection
from rest_framework import status
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
from general_info.serializers import GeneralInfoSerializer
from courses.models import Courses
from courses.serializers import CoursesSerializer
from spec_check.models import SpecCheck
from spec_check.serializers import SpecCheckSerializer
from attestation.models import Attestation
from attestation.serializers import AttestationSerializer
from awards.models import Awards
from awards.serializers import AwardsSerializer
from investigation_retrieval.models import InvestigationRetrieval
from investigation_retrieval.serializers import InvestigationRetrievalSerializer
from class_category.models import ClassCategory
from class_category.serializers import ClassCategorySerializer
from sick_leaves.models import SickLeaves
from sick_leaves.serializers import SickLeavesSerializer
from orders_list.models import OrdersList
from orders_list.serializers import OrdersListSerializer
from working_history.models import WorkingHistory
from working_history.serializers import WorkingHistorySerializer
from military_rank.models import MilitaryRank
from military_rank.serializers import MilitaryRankSerializer


class ReportListAPIView(ListAPIView):
    available_models = {'general_info': GeneralInfo,
                        'personal_data': PersonalData,
                        'family_compositions': FamilyComposition,
                        'educations': Education,
                        'owning_languages': OwningLanguages,
                        'courses': Courses,
                        'academic_degree': AcademicDegree,
                        'sport_results': SportResults,
                        'spec_checks': SpecCheck,
                        'attestations': Attestation,
                        'awards': Awards,
                        'investigation_retrievals': InvestigationRetrieval,
                        'class_categories': ClassCategory,
                        'sick_leaves': SickLeaves,
                        'orders_list': OrdersList,
                        'working_histories': WorkingHistory,
                        'military_ranks': MilitaryRank,
                        }

    available_serializers = {'general_info': GeneralInfoSerializer,
                             'personal_data': PersonalDataSerializer,
                             'family_compositions': FamilyCompositionSerializer,
                             'educations': EducationSerializer,
                             'owning_languages': OwningLanguagesSerializer,
                             'courses': CoursesSerializer,
                             'academic_degree': AcademicDegreeSerializer,
                             'sport_results': SportResultSerializers,
                             'spec_checks': SpecCheckSerializer,
                             'attestations': AttestationSerializer,
                             'awards': AwardsSerializer,
                             'investigation_retrievals': InvestigationRetrievalSerializer,
                             'class_categories': ClassCategorySerializer,
                             'sick_leaves': SickLeavesSerializer,
                             'orders_list': OrdersListSerializer,
                             'working_histories': WorkingHistorySerializer,
                             'military_ranks': MilitaryRankSerializer,
                             }

    serializer_class = GeneralInfoSerializer

    def get_queryset(self):
        sql_query = """
            SELECT * from general_info
            INNER JOIN family_composition ON family_composition.iin_id = general_info.id
            """

        queryset = GeneralInfo.objects.raw(sql_query)
        print(queryset)
        return queryset
        # response_data = GeneralInfo.objects.raw("SELECT * FROM ")




        # if id is None:
        #     return Response({'message': 'Введите корректный ID'}, status=status.HTTP_400_BAD_REQUEST)
        #
        # try:
        #     general_info = GeneralInfo.objects.get(id=id)
        # except:
        #     return Response({'message': 'Пользователь с таким ID не найден'}, status=status.HTTP_404_NOT_FOUND)
        #
        # response_data = {}
        #
        # for related_name, serializer in self.available_serializers.items():
        #     related_queryset = getattr(general_info, related_name).all()
        #     if related_name != 'personal_data':
        #         response_data[related_name] = serializer(related_queryset, many=True).data
        #     else:
        #         if (len(related_queryset)) >= 1:
        #             response_data[related_name] = serializer(related_queryset[0]).data
        #         else:
        #             response_data[related_name] = {}

        # return Response(response_data, status=status.HTTP_200_OK)
