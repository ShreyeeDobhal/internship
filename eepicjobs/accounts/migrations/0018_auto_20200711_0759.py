# Generated by Django 2.2.2 on 2020-07-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_settime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionpack',
            name='subscriptionid',
            field=models.CharField(choices=[('499 per month', '499 per month'), ('700 for two months', '700 for two months'), ('Yearly subscription @3400', 'Yearly subscription @3400')], default='499 per month', max_length=20),
        ),
    ]
