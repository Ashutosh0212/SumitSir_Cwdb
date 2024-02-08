from rest_framework import serializers
from authapp.models import Proposal

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['user', 'name_and_address', 'project_scheme']