# Generated by Django 3.2.3 on 2021-10-20 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_busname_seat_busname'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='seatNum',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]