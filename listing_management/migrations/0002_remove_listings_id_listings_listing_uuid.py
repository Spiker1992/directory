# Generated by Django 5.0.1 on 2024-06-13 23:06

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('listing_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='id',
        ),
        migrations.AddField(
            model_name='listings',
            name='listing_uuid',
            field=models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
