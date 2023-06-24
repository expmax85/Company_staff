from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import OpenApiExample, extend_schema

from departments.models import Employer, Department
from departments.serializers import EmployerSerializer, DepartmentSerializer


class EmployerViewSet(ModelViewSet):
    queryset = Employer.objects.select_related('department').all()
    serializer_class = EmployerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "surname",
        "department__id",
    ]

    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        ret = serializer.data
        ret['full_name'] = ' '.join([ret.pop('surname'), ret.pop('first_name'), ret.pop('second_name')])
        return Response(ret)


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    @extend_schema(
        examples=[
            OpenApiExample(
                'Valid example',
                summary='department example',
                value=[
                        {
                        "id": 1,
                        "first_name": "Ivanov",
                        "surname": "Ivan",
                        "second_name": "Ivanovich",
                        "photo": "string",
                        "job_title": "worker",
                        "salary": "10000",
                        "age": 30,
                        "department": 1
                    },
                ],
            ),
        ]
    )
    @action(detail=True, methods=['get'])
    def employers(self, request: Request, pk=None) -> Response:
        employers = self.get_object().employers.all()
        serializer = EmployerSerializer(employers, many=True)
        return Response(serializer.data)
