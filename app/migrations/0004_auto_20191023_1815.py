# Generated by Django 2.0.2 on 2019-10-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191022_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='pic',
        ),
        migrations.AddField(
            model_name='student',
            name='pic1',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic10',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic11',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic12',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic13',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic14',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic15',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic2',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic3',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic4',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic5',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic6',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic7',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic8',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
        migrations.AddField(
            model_name='student',
            name='pic9',
            field=models.ImageField(blank=True, upload_to='student_pic/'),
        ),
    ]