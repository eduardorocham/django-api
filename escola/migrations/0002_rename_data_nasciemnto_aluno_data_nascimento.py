# Generated by Django 4.2.7 on 2023-11-22 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='data_nasciemnto',
            new_name='data_nascimento',
        ),
    ]