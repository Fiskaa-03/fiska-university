# Generated by Django 4.1.3 on 2023-05-22 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Students_Data',
            fields=[
                ('NIM', models.CharField(editable=False, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('contact', models.IntegerField(max_length=20)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='students.major_data')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='students.status_data')),
            ],
        ),
    ]
