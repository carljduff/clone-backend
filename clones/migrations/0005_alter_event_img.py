# Generated by Django 4.0.4 on 2022-04-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clones', '0004_event_guests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]