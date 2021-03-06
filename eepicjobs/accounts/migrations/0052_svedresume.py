# Generated by Django 2.2.2 on 2020-07-28 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0051_set_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Svedresume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aplid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.applicantt')),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Employer')),
            ],
            options={
                'verbose_name': 'Svedresume',
                'verbose_name_plural': 'Svedresumes',
            },
        ),
    ]
