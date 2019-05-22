# Generated by Django 2.1.7 on 2019-05-22 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190518_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidentifiedAttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, unique=True)),
                ('attendance_record', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='attendancerecord',
            old_name='register',
            new_name='attendance_record',
        ),
    ]
