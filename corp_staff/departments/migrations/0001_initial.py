# Generated by Django 4.2.2 on 2023-06-23 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('job_title', models.CharField(max_length=255)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('age', models.PositiveSmallIntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employers', to='departments.department')),
            ],
            options={
                'unique_together': {('department', 'id')},
            },
        ),
        migrations.AddField(
            model_name='department',
            name='director',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director_department', to='departments.employer'),
        ),
    ]