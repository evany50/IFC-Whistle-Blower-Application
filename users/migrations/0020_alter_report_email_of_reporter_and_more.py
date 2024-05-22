# Generated by Django 5.0.2 on 2024-03-16 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_user_rolls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='email_of_reporter',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='report',
            name='location_of_incident',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='report',
            name='name_of_reporter',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='organization_of_reporter',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='phone_num_of_reporter',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='rolls',
            field=models.CharField(choices=[('IFC JC Admin', 'IFC JC Admin'), ('Anonymous', 'Anonymous'), ('Common', 'Common'), ('IFC JC Counselor', 'IFC JC Counselor'), ('Django Admin', 'Django Admin')], default='Common', max_length=20),
        ),
    ]
