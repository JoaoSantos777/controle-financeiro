# Generated by Django 5.0.6 on 2024-09-03 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Politico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('cargo', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partido.partido')),
            ],
        ),
    ]
