# Generated by Django 4.2 on 2023-04-26 06:31

from django.db import migrations, models
import todo.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todol',
            name='due_date',
            field=models.DateTimeField(default=todo.models.one_week),
        ),
    ]