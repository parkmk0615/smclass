# Generated by Django 5.1.3 on 2024-11-28 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cpw',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
