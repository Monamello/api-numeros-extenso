# Generated by Django 2.1.7 on 2019-02-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='numero',
            name='extenso',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
