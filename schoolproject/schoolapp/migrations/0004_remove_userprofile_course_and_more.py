# Generated by Django 4.2.6 on 2023-12-06 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0003_material_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='course',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='department',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='materials_provided',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
