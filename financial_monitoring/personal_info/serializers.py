from rest_framework import serializers
from personal_data.serializers import PersonalDataSerializer
from family_composition.serializers import FamilyCompositionSerializer
from education.serializers import EducationSerializer
from owning_languages.serializers import OwningLanguagesSerializer
from academic_degree.serializers import AcademicDegreeSerializer
from sport_results.serializers import SportResultSerializers
from courses.serializers import CoursesSerializer


class PersonalInfoSerializer(serializers.Serializer):
    personal_data = PersonalDataSerializer()
    family_composition = FamilyCompositionSerializer()
    education = EducationSerializer(many=True)
    courses = CoursesSerializer()
    owning_languages = OwningLanguagesSerializer()
    academic_degree = AcademicDegreeSerializer()
    sport_results = SportResultSerializers()
    
