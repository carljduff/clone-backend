# Generated by Django 4.0.4 on 2022-04-27 18:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clones', '0009_alter_event_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(null=True, related_name='guests', to=settings.AUTH_USER_MODEL),
        ),
    ]