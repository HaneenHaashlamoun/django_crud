# Generated by Django 3.2.9 on 2021-11-20 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snacks', '0002_auto_20211120_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='purchaser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
