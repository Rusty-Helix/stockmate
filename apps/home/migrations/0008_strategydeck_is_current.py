# Generated by Django 3.2.16 on 2023-07-04 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20230627_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategydeck',
            name='is_current',
            field=models.BooleanField(default=False),
        ),
    ]
