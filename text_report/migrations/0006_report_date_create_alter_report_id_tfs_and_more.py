# Generated by Django 4.2.7 on 2023-12-02 20:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('text_report', '0005_alter_report_floating_defect'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date_create',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='id_tfs',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='report',
            name='my_solution',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]