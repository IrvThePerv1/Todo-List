# Generated by Django 4.2 on 2023-04-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_rename_host_todol_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todol',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]