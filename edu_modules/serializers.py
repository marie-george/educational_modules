from rest_framework import serializers

from edu_modules.models import EduModule


class EduModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduModule
        fields = '__all__'
