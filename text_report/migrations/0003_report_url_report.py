# Generated by Django 4.2.7 on 2023-12-02 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_report', '0002_alter_report_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='url_report',
            field=models.URLField(blank=True, null=True),
        ),
    ]
