# Generated by Django 4.2 on 2023-04-26 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todol_host_alter_todol_due_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todol',
            old_name='host',
            new_name='user',
        ),
    ]
