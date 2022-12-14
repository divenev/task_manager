# Generated by Django 4.1.4 on 2022-12-14 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webtask', '0005_alter_step_status_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='machine_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='webtask.machine'),
        ),
        migrations.AlterField(
            model_name='step',
            name='personnel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='webtask.personnel', verbose_name='Executor'),
        ),
        migrations.AlterField(
            model_name='step',
            name='task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='webtask.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='personnel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='webtask.personnel', verbose_name='Manager'),
        ),
        migrations.AlterField(
            model_name='task',
            name='profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
    ]
