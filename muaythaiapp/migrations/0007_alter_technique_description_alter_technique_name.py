# Generated by Django 4.2.1 on 2023-06-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muaythaiapp', '0006_alter_trainingdrill_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technique',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='technique',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
