# Generated by Django 3.2.4 on 2021-06-17 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_rename_text_todo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(max_length=30, null=True),
        ),
    ]