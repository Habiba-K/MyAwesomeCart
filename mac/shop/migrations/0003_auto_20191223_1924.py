# Generated by Django 3.0.1 on 2019-12-23 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20191222_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Other_features',
            new_name='category',
        ),
    ]