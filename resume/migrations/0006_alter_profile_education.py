# Generated by Django 5.1.1 on 2024-09-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_rename_workexp_profile_workexperience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.TextField(),
        ),
    ]
