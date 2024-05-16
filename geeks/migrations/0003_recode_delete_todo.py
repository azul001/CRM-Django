# Generated by Django 5.0.6 on 2024-05-14 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0002_remove_todo_created_date_remove_todo_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('adderss', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='todo',
        ),
    ]
