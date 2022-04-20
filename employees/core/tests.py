import json
import datetime

from django.db import connection
from django.test.utils import CaptureQueriesContext
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.serializers import EmployeesSerializer
from core.models import Employee


class EmployeesApiTestCase(APITestCase):
    def setUp(self):
        self.employee1 = Employee.objects.create(
            first_name='Petr',
            last_name='Petrov',
            date_of_birth='2000-01-01',
            date_of_employment='2022-01-01'
        )
        self.employee2 = Employee.objects.create(
            first_name='Stas',
            last_name='Stasov',
            date_of_birth='2001-02-03',
            date_of_employment='2021-01-01'
        )
        self.employee3 = Employee.objects.create(
            first_name='Max',
            last_name='Maxov',
            date_of_birth='1990-01-01',
            date_of_employment='2019-10-01'
        )
        self.employee4 = Employee.objects.create(
            first_name='Ivan',
            last_name='Ivanov',
            date_of_birth='1980-01-31',
            date_of_employment='2005-01-01'
        )
        self.employee5 = Employee.objects.create(
            first_name='Sergey',
            last_name='Sergeev',
            date_of_birth='1992-10-08',
            date_of_employment='2020-01-01'
        )

    def test_get(self):
        url = reverse('select-list')

        with CaptureQueriesContext(connection) as queries:
            response = self.client.get(url)
            self.assertEqual(1, len(queries))

        employees = Employee.objects.all().order_by('date_of_birth')
        serializer_data = EmployeesSerializer(employees, many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_single(self):
        url = reverse('select-detail', args=[self.employee5.pk])

        with CaptureQueriesContext(connection) as queries:
            response = self.client.get(url)
            self.assertEqual(1, len(queries))

        employee = Employee.objects.filter(pk=self.employee5.pk).first()
        serializer_data = EmployeesSerializer(employee).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        objects_before = Employee.objects.all().count()
        url = reverse('insert')
        data = {
            'first_name': 'Nikolay',
            'last_name': 'Nikolaev',
            'date_of_birth': '1995-05-05',
            'date_of_employment': '2015-10-01'
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(objects_before + 1, Employee.objects.all().count())

    def test_update(self):
        self.employee2.refresh_from_db()

        url = reverse('update-detail', args=[self.employee2.pk])

        data = {
            'first_name': self.employee2.first_name,
            'last_name': self.employee2.last_name,
            'date_of_birth': str(self.employee2.date_of_birth),
            'date_of_employment': str(datetime.date(2014, 9, 1))
        }
        json_data = json.dumps(data)
        response = self.client.put(url, data=json_data, content_type='application/json')

        self.employee2.refresh_from_db()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('2014-09-01', str(self.employee2.date_of_employment))
