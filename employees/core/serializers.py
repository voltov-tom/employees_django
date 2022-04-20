from rest_framework.serializers import ModelSerializer

from core.models import Employee


class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
