from django.contrib import admin

from .models import Department, Employer


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', '_director_')

    def _director_(self, obj: Department) -> str:
        if not obj.director:
            return 'vacancy'
        return obj.director


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')

    def name(self, obj: Employer) -> str:
        return " ".join([obj.first_name, obj.surname, obj.second_name])
