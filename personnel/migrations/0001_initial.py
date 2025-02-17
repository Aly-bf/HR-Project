# Generated by Django 3.1.12 on 2025-01-24 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('fathername', models.CharField(max_length=50)),
                ('milirary_status', models.BooleanField(default=False)),
                ('martial_status', models.BooleanField(default=False)),
                ('degree', models.CharField(choices=[('bachelor', 'Bachelor'), ('master', 'Master'), ('phd', 'Phd')], max_length=50)),
                ('employment_data', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
