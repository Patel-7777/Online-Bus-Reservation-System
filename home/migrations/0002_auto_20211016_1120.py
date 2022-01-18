# Generated by Django 3.2.3 on 2021-10-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbus',
            name='s1fare',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='addbus',
            name='s2fare',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='addbus',
            name='s3fare',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='addbus',
            name='s4fare',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='addbus',
            name='fare',
            field=models.IntegerField(default=0),
        ),
    ]