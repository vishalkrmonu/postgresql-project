# Generated by Django 5.1.2 on 2024-10-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='college_name',
            field=models.CharField(max_length=200),
        ),
    ]
