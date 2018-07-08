# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 21:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('djangocms_work', '0003_remove_category_name2'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_work', to=settings.FILER_IMAGE_MODEL),
        ),
    ]