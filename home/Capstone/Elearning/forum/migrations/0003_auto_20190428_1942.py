# Generated by Django 2.1.8 on 2019-04-28 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_posted']},
        ),
    ]
