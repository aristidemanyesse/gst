# Generated by Django 4.2.9 on 2024-01-17 10:07

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_employe_created_at_employe_deleted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employe',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='newletter',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='employe',
            name='protected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employe',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='newletter',
            name='contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='newletter',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newletter',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newletter',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='newletter',
            name='protected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newletter',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='newletter',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='newletter',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employe',
            name='photo',
            field=models.ImageField(blank=True, default=0, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='newletter',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
