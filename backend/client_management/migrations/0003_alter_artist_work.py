# Generated by Django 4.1.7 on 2023-02-23 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_management', '0002_alter_work_work_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='work',
            field=models.ManyToManyField(related_name='work', through='client_management.Assignment', to='client_management.work'),
        ),
    ]
