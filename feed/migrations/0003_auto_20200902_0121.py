# Generated by Django 3.0.9 on 2020-09-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20200902_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.TextField(default='', max_length=200, null=True),
        ),
    ]
