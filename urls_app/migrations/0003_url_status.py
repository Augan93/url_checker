# Generated by Django 3.1.1 on 2020-09-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls_app', '0002_url_is_paused'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]