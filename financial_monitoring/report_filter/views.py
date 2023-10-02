from rest_framework.generics import ListAPIView
from django.db import connection
from datetime import datetime, date
from django.db.models import Q
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
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


class ReportListAPIView(APIView):
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

    field_to_model = {
        model_field.name: model_name for model_name, model in available_models.items() for model_field in model._meta.fields
    }

    # pagination_class = PageNumberPagination

    def get(self, request, format=None):
        response_data = []
        model_fields_filter = {}

        for field_name, field_value in request.query_params.items():
            if field_name == "page":
                continue
            if self.field_to_model[field_name] not in model_fields_filter:
                 model_fields_filter[self.field_to_model[field_name]] = {}
            model_fields_filter[self.field_to_model[field_name]][field_name] = field_value

        general_infos = GeneralInfo.objects.all()

        if "general_info" in model_fields_filter:
            q_objects = Q()
            for field_name, field_value in model_fields_filter["general_info"].items():
                filter_dict = {f"{field_name}__icontains": field_value}
                q_objects &= Q(**filter_dict)
                related_queryset = GeneralInfo.objects.filter(q_objects)
                general_infos = related_queryset

        model_fields_filter.pop("general_info", None)

        for general_info in general_infos:
            current_data = {"general_info": self.available_serializers["general_info"](general_info).data}
            for related_name, fields_filter in model_fields_filter.items():
                related_queryset = getattr(general_info, related_name).all()
                q_objects = Q()

                for field in fields_filter:
                    field_object = related_queryset.model._meta.get_field(field)
                    field_type = field_object.get_internal_type()

                    if field_type == "DateField":
                        start_date, end_date = fields_filter[field].split(':')

                        start_date = datetime.strptime(start_date, '%Y-%m-%d') if start_date else None
                        end_date = datetime.strptime(end_date, '%Y-%m-%d') if end_date else None

                        if start_date:
                            filter_dict = {f"{field}__gte":  start_date}
                            q_objects &= Q(**filter_dict)

                        if end_date:
                            filter_dict = {f"{field}__lte": end_date}
                            q_objects &= Q(**filter_dict)

                    else:
                        filter_dict = {f"{field}__icontains": fields_filter[field]}
                        q_objects &= Q(**filter_dict)

                related_queryset = related_queryset.filter(q_objects)
                # print(f" {related_name } : related_queryset")

                if len(related_queryset):
                    current_data[related_name] = self.available_serializers[related_name](related_queryset, many=True).data
            response_data.append(current_data)

        # paginator = self.pagination_class()
        # paginated_data = paginator.paginate_queryset(response_data, request)
        # return paginator.get_paginated_response(paginated_data)

        return Response(response_data, status=status.HTTP_200_OK)
