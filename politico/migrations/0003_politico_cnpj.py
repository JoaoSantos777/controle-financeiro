# Generated by Django 5.1.1 on 2024-09-06 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politico', '0002_alter_politico_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='politico',
            name='cnpj',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]