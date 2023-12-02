# Generated by Django 4.2.7 on 2023-12-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('platform_name', models.CharField(choices=[('1', 'hw-10-f1'), ('2', 'hw-100-n1'), ('3', 'hw-100-n2'), ('4', 'hw-100-n3'), ('5', 'hw-100-x3'), ('6', 'hw-100-x8'), ('7', 'hw-1000-q1'), ('8', 'hw-1000-q2'), ('9', 'hw-1000-q3'), ('10', 'hw-1000-q4'), ('11', 'hw-1000-q5'), ('12', 'hw-1000-q6'), ('13', 'hw-1000-q7'), ('14', 'hw-1000-q8'), ('15', 'hw-2000-q2'), ('16', 'hw-2000-q3'), ('17', 'hw-2000-q4'), ('18', 'hw-50-n1'), ('19', 'hw-50-n2'), ('20', 'hw-50-n3'), ('21', 'hw-50-n4'), ('22', 'va-10'), ('23', 'va-100'), ('24', 'va-1000')], default='1', max_length=20)),
                ('build_number', models.IntegerField()),
                ('problem', models.TextField()),
                ('my_solution', models.TextField()),
            ],
        ),
    ]