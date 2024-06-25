# Generated by Django 5.0.6 on 2024-06-17 23:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0002_sitesetup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesetup',
            options={'verbose_name': 'Setup', 'verbose_name_plural': 'Setup'},
        ),
        migrations.AddField(
            model_name='menulink',
            name='site_setup',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='site_setup.sitesetup'),
        ),
    ]
