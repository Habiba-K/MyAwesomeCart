# Generated by Django 3.0.1 on 2019-12-23 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20191223_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Other_features',
            field=models.CharField(default='', max_length=300),
        ),
    ]
