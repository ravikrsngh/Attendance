# Generated by Django 2.0.2 on 2019-11-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191102_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
