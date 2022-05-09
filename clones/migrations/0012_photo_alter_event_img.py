# Generated by Django 4.0.4 on 2022-05-07 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clones', '0011_alter_event_guests'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='', upload_to='clones/images/')),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='img',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clones.photo'),
        ),
    ]