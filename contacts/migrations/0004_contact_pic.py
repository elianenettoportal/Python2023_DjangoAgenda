# Generated by Django 4.1.7 on 2023-03-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='pic',
            field=models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d'),
        ),
    ]