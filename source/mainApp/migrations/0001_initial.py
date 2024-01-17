# Generated by Django 4.2.9 on 2024-01-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('prenoms', models.CharField(blank=True, max_length=255, null=True)),
                ('fonction', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.IntegerField(blank=True, default=0, null=True)),
                ('photo', models.IntegerField(blank=True, default=0, null=True)),
                ('qrcode', models.IntegerField(blank=True, default=0, null=True)),
                ('started', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
