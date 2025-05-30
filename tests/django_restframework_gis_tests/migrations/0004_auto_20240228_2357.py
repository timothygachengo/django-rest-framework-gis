# Generated by Django 3.2.24 on 2024-02-28 22:57

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("django_restframework_gis_tests", "0003_schema_models"),
    ]

    operations = [
        migrations.AlterField(
            model_name="boxedlocation",
            name="geometry",
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326),
        ),
        migrations.AlterField(
            model_name="locatedfile",
            name="geometry",
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326),
        ),
        migrations.AlterField(
            model_name="location",
            name="geometry",
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326),
        ),
    ]
