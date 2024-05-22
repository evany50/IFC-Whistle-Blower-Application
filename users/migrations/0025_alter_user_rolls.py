# Generated by Django 4.2.11 on 2024-03-18 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_reportfile_file_alter_user_rolls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rolls',
            field=models.CharField(choices=[('Common', 'Common'), ('IFC JC Admin', 'IFC JC Admin'), ('Anonymous', 'Anonymous'), ('IFC JC Counselor', 'IFC JC Counselor'), ('Django Admin', 'Django Admin')], default='Common', max_length=20),
        ),
    ]
