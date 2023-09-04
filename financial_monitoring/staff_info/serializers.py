from rest_framework import serializers
from spec_check.serializers import SpecCheckSerializer
from attestation.serializers import AttestationSerializer
from awards.serializers import AwardsSerializer
from investigation_retrieval.serializers import InvestigationRetrievalSerializer
from class_category.serializers import ClassCategorySerializer
from autobiography.serializers import AutobiographySerializer
from sick_leaves.serializers import SickLeavesSerializer


class StaffInfoSerializer(serializers.Serializer):
    spec_check = SickLeavesSerializer(many=True)
    attestation = AttestationSerializer(many=True)
    awards = AwardsSerializer(many=True)
    investigation_retrieval = InvestigationRetrievalSerializer(many=True)
    class_category = ClassCategorySerializer(many=True)
    autobiography = AutobiographySerializer()
    sick_leaves = SickLeavesSerializer(many=True)