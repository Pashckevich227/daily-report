# Generated by Django 4.2.7 on 2023-12-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_report', '0009_alter_report_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date_create',
            field=models.DateField(auto_now_add=True),
        ),
    ]