# Generated by Django 3.2.5 on 2021-08-01 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='block_prev_hash',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
