from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=50)
    director = models.OneToOneField('Employer', on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name='director_department')

    def __str__(self):
        return self.title


class Employer(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos', null=True, blank=True)
    job_title = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    age = models.PositiveSmallIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employers')

    class Meta:
        unique_together = ('department', 'id')

    def __str__(self):
        return " ".join([str(self.first_name), str(self.surname), str(self.second_name)])
