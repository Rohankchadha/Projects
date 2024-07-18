# Generated by Django 4.1.5 on 2023-03-02 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_mdl_inquiry_mdl_attach_mdl_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mdl',
            name='attach',
        ),
        migrations.AddField(
            model_name='mdl',
            name='files',
            field=models.FileField(default='', upload_to='files/'),
        ),
        migrations.AddField(
            model_name='mdl',
            name='images',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
