# Generated by Django 4.2.4 on 2023-08-27 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='updated_date',
        ),
    ]
