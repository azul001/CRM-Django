# Generated by Django 5.0.6 on 2024-05-14 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0004_rename_adderss_recode_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='recode',
            name='Email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
