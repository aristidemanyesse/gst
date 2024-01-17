# Generated by Django 4.2.9 on 2024-01-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_alter_employe_options_alter_newletter_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe',
            name='started',
        ),
        migrations.AlterField(
            model_name='employe',
            name='photo',
            field=models.ImageField(blank=True, default='images/profiles/default.png', max_length=255, null=True, upload_to='images/profiles/'),
        ),
        migrations.AlterField(
            model_name='employe',
            name='qrcode',
            field=models.ImageField(blank=True, default='images/qrcodes/default.png', max_length=255, null=True, upload_to='images/qrcodes/'),
        ),
    ]