# Generated by Django 3.2.5 on 2021-08-01 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('block', '0002_alter_block_block_prev_hash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='signers',
        ),
        migrations.AddField(
            model_name='block',
            name='signers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
