# Generated by Django 3.2.8 on 2021-11-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20211105_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='Website_link',
            field=models.CharField(default='', max_length=30),
        ),
    ]
