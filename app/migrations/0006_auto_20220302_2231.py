# Generated by Django 3.2.12 on 2022-03-03 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_volunteer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentialing',
            name='peer_reviewer_1',
            field=models.CharField(blank=True, help_text='enter peer review email address', max_length=100),
        ),
        migrations.AlterField(
            model_name='credentialing',
            name='peer_reviewer_2',
            field=models.CharField(blank=True, help_text='enter peer review email address', max_length=100),
        ),
        migrations.AlterField(
            model_name='credentialing',
            name='peer_reviewer_3',
            field=models.CharField(blank=True, help_text='enter peer review email address', max_length=100),
        ),
    ]