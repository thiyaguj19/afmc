# Generated by Django 3.2.12 on 2022-02-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_activities_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentialing',
            name='year',
            field=models.IntegerField(help_text='enter year of Credentialing', max_length=4),
        ),
    ]