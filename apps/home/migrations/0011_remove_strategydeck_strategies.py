# Generated by Django 3.2.16 on 2023-07-04 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20230704_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strategydeck',
            name='strategies',
        ),
    ]
