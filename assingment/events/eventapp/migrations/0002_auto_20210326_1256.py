# Generated by Django 3.1.1 on 2021-03-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_template',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.CharField(default='', max_length=6)),
                ('month', models.CharField(default='', max_length=16)),
                ('start_time', models.CharField(default='', max_length=6)),
                ('end_time', models.CharField(default='', max_length=6)),
                ('location', models.CharField(default='', max_length=16)),
                ('details', models.CharField(default='', max_length=100)),
                ('image1', models.ImageField(default='', upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Slider1',
        ),
    ]
