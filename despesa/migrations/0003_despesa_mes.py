# Generated by Django 5.1.1 on 2025-01-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0002_alter_despesa_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='mes',
            field=models.DateField(blank=True, null=True, verbose_name='Mês de Referência'),
        ),
    ]
