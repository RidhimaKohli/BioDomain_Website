# Generated by Django 3.2.8 on 2021-11-05 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_remove_instruments_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='instruments',
            name='Category',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='website.category_description'),
            preserve_default=False,
        ),
    ]