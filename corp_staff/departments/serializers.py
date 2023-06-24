from django.db.models import Sum
from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample, extend_schema_serializer, extend_schema

from .models import Department, Employer


@extend_schema_serializer(
    examples=[
         OpenApiExample(
            'Valid example',
            summary='employer example',
            value={
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
         ),
    ]
)
class EmployerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employer
        fields = '__all__'


@extend_schema_serializer(
    examples=[
         OpenApiExample(
            'Valid example',
            summary='department example',
            value={
                "id": 1,
                "title": "IT Depart",
                "director": 1,
                "count_staff": 2,
                "sum_salary": 1000
              },
         ),
    ]
)
class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'

    def to_representation(self, instance: Department) -> dict:
        ret = super().to_representation(instance)
        ret['count_staff'] = instance.employers.count()
        ret.update(instance.employers.aggregate(sum_salary=Sum('salary')))
        return ret
