# Generated by Django 2.2.17 on 2021-06-02 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0026_auto_20210602_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='sem',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='sub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='attendence.Subject'),
        ),
    ]
