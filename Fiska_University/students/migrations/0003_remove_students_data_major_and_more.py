# Generated by Django 4.1.3 on 2023-05-22 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_students_data_id_alter_students_data_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students_data',
            name='major',
        ),
        migrations.RemoveField(
            model_name='students_data',
            name='status',
        ),
        migrations.DeleteModel(
            name='Major_Data',
        ),
        migrations.DeleteModel(
            name='Status_Data',
        ),
        migrations.DeleteModel(
            name='Students_Data',
        ),
    ]
