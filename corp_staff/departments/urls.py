from rest_framework.routers import DefaultRouter

from departments.views import EmployerViewSet, DepartmentViewSet


router = DefaultRouter()
router.register("employers", EmployerViewSet)
router.register("departments", DepartmentViewSet)
