# Generated by Django 4.1.4 on 2022-12-13 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtask', '0003_alter_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='step_priority',
            field=models.PositiveIntegerField(),
        ),
    ]
