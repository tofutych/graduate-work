# Generated by Django 4.1.1 on 2022-09-23 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'db_table': 'faculty',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=20)),
                ('slug', models.SlugField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievement.faculty')),
            ],
            options={
                'db_table': 'speciality',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='YearOfAdmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022)),
                ('slug', models.SlugField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievement.faculty')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievement.speciality')),
            ],
            options={
                'db_table': 'year_of_admission',
                'ordering': ('year',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievement.faculty')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievement.speciality')),
                ('year_of_admission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievement.yearofadmission')),
            ],
            options={
                'db_table': 'student',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('url', models.URLField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievement.student')),
            ],
            options={
                'db_table': 'achievement',
                'ordering': ('-date_added',),
            },
        ),
    ]
