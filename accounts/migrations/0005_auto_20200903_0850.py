# Generated by Django 3.0.9 on 2020-09-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200903_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default1.jpg', upload_to='profile_picture'),
        ),
    ]
