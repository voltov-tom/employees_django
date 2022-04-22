from rest_framework.serializers import ModelSerializer

from core.models import Employee


class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = 'id', 'first_name', 'last_name', 'date_of_birth', 'date_of_employment', 'work_experience',


class EmployeesUpdateSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
