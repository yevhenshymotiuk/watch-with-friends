# Generated by Django 3.0 on 2019-12-27 17:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20191218_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='slug',
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
