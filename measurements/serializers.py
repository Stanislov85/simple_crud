from rest_framework import serializers
from .models import Project, Measurement


class ProjectSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class MeasurementSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'