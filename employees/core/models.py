from django.db import models
from django.utils.timezone import now


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_employment = models.DateField()

    @property
    def work_experience(self):
        today_date = now().date()
        date_of_employment = self.date_of_employment
        return (today_date.year - date_of_employment.year) * 12 + (today_date.month - date_of_employment.month)
