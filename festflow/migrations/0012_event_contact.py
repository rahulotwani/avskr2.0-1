# Generated by Django 2.0.2 on 2018-10-13 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0011_event_tiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
