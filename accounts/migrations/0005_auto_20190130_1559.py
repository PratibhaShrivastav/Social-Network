# Generated by Django 2.1.4 on 2019-01-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190130_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to='images/'),
        ),
    ]
