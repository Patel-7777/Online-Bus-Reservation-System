# Generated by Django 3.2.3 on 2021-10-14 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bname', models.CharField(max_length=50)),
                ('PickUp', models.TextField()),
                ('ptime', models.TimeField()),
                ('dest', models.TextField()),
                ('dtime', models.TimeField()),
                ('s1name', models.TextField()),
                ('s1time', models.TimeField()),
                ('s2name', models.TextField()),
                ('s2time', models.TimeField()),
                ('s3name', models.TextField()),
                ('s3time', models.TimeField()),
                ('s4name', models.TextField()),
                ('s4time', models.TimeField()),
                ('Btype', models.TextField()),
                ('fare', models.IntegerField()),
            ],
        ),
    ]
