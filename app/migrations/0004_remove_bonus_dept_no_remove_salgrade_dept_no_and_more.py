# Generated by Django 4.2.6 on 2023-12-25 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_employee_emp_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonus',
            name='dept_no',
        ),
        migrations.RemoveField(
            model_name='salgrade',
            name='dept_no',
        ),
        migrations.AddField(
            model_name='bonus',
            name='emp_salary',
            field=models.OneToOneField(default=1000, on_delete=django.db.models.deletion.CASCADE, to='app.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salgrade',
            name='emp_salary',
            field=models.OneToOneField(default=10000, on_delete=django.db.models.deletion.CASCADE, to='app.employee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salgrade',
            name='highsal',
            field=models.IntegerField(default=10000),
        ),
        migrations.AlterField(
            model_name='salgrade',
            name='lowsal',
            field=models.IntegerField(default=1000),
        ),
    ]
