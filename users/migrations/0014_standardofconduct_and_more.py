# Generated by Django 5.0.2 on 2024-03-15 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_report_phone_num_of_reporter_alter_user_rolls'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardOfConduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='violated_standards_conduct',
        ),
        migrations.AlterField(
            model_name='user',
            name='rolls',
            field=models.CharField(choices=[('Django Admin', 'Django Admin'), ('IFC JC Counselor', 'IFC JC Counselor'), ('IFC JC Admin', 'IFC JC Admin'), ('Common', 'Common'), ('Anonymous', 'Anonymous')], default='Common', max_length=20),
        ),
        migrations.AddField(
            model_name='report',
            name='violated_standards_conduct',
            field=models.ManyToManyField(to='users.standardofconduct'),
        ),
    ]
