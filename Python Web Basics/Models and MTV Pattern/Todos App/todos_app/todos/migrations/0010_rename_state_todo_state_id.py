# Generated by Django 3.2.4 on 2021-06-17 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0009_alter_todo_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='state',
            new_name='state_id',
        ),
    ]
