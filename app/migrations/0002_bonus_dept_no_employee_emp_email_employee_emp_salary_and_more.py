# Generated by Django 4.2.6 on 2023-12-12 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonus',
            name='dept_no',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.dept'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_salary',
            field=models.IntegerField(default=5000),
        ),
        migrations.AddField(
            model_name='salgrade',
            name='dept_no',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.dept'),
            preserve_default=False,
        ),
    ]
