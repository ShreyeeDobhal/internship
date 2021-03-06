# Generated by Django 2.2.2 on 2020-07-26 12:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0047_auto_20200723_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='ad',
            field=models.CharField(choices=[('Feature', 'Feature'), ('Premium', 'Premium')], default='Feature', max_length=255, verbose_name='select your add type, (chose premium only if you have a subscription pack)'),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='no_of_employees',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='salary_beg',
            field=models.FloatField(default=0.0, verbose_name='Give the initial sal range'),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='salary_end',
            field=models.FloatField(default=0.0, verbose_name='Give the end of sal range'),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='updates_email',
            field=models.EmailField(max_length=254, null=True, validators=[django.core.validators.EmailValidator], verbose_name='Daily updates about this job and candidates will be sent to:'),
        ),
    ]
