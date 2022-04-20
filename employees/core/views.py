from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from core.models import Employee
from core.serializers import EmployeesSerializer


class EmployeesListView(ModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = Employee.objects.all().order_by('date_of_birth')
    serializer_class = EmployeesSerializer


class EmployeeInsertView(GenericAPIView, CreateModelMixin):
    serializer_class = EmployeesSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeUpdateView(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
