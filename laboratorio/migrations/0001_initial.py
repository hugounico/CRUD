# Generated by Django 3.2.1 on 2023-09-29 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('ciudad', models.CharField(default='Santiago', max_length=100)),
                ('pais', models.CharField(default='Chile', max_length=100)),
            ],
            options={
                'db_table': 'Laboratorio',
            },
        ),
    ]
