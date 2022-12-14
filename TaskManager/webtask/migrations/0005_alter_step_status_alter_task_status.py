# Generated by Django 4.1.4 on 2022-12-14 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtask', '0004_alter_step_step_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('in_progress', 'in_progress'), ('returned', 'returned'), ('frozen', 'frozen'), ('closed', 'closed')], default='created', max_length=25),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('in_progress', 'in_progress'), ('frozen', 'frozen'), ('closed', 'closed')], default='created', max_length=25),
        ),
    ]
