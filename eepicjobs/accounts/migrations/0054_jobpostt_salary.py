# Generated by Django 2.2.2 on 2020-07-29 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0053_jobpostt_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpostt',
            name='salary',
            field=models.CharField(max_length=455, null=True),
        ),
    ]
