# Generated by Django 4.0.5 on 2023-07-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_delete_phrase_paid_private_phrase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paid',
            name='private_phrase',
            field=models.TextField(blank=True, default=''),
        ),
    ]
