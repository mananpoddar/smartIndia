# Generated by Django 2.1.7 on 2019-03-03 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fraud', '0005_remove_aadhar_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictions',
            name='predicted_features',
        ),
        migrations.AddField(
            model_name='predicted_features',
            name='fraud',
            field=models.BooleanField(default=0),
        ),
        migrations.DeleteModel(
            name='predictions',
        ),
    ]
