from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from core.views import EmployeesListView, EmployeeInsertView, EmployeeUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/', EmployeeInsertView.as_view(), name='insert'),
]

router = SimpleRouter()
router.register(r'select', EmployeesListView, basename='select')
router.register(r'update', EmployeeUpdateView, basename='update')

urlpatterns += router.urls
