# Generated by Django 4.0 on 2021-12-12 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0002_imovel_ativo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imovel',
            name='observacao',
        ),
    ]
