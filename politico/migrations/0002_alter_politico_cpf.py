# Generated by Django 5.0.6 on 2024-09-04 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politico',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
