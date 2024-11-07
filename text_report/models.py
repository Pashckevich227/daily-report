from django.db import models


# Create your models here.
class Report(models.Model):
    PLATFORMS = [
        ('1', 'hw-10-f1'),
        ('2', 'hw-100-n1'),
        ('3', 'hw-100-n2'),
        ('4', 'hw-100-n3'),
        ('5', 'hw-100-x3'),
        ('6', 'hw-100-x8'),
        ('7', 'hw-1000-q1'),
        ('8', 'hw-1000-q2'),
        ('9', 'hw-1000-q3'),
        ('10', 'hw-1000-q4'),
        ('11', 'hw-1000-q5'),
        ('12', 'hw-1000-q6'),
        ('13', 'hw-1000-q7'),
        ('14', 'hw-1000-q8'),
        ('15', 'hw-2000-q2'),
        ('16', 'hw-2000-q3'),
        ('17', 'hw-2000-q4'),
        ('18', 'hw-50-n1'),
        ('19', 'hw-50-n2'),
        ('20', 'hw-50-n3'),
        ('21', 'hw-50-n4'),
        ('22', 'va-10'),
        ('23', 'va-100'),
        ('24', 'va-1000')
    ]

    BUG = [
        ('1', 'Дефект продукта'),
        ('2', 'Дефект автостенда'),
        ('3', 'Новый дефект'),
        ('4', 'Доработка автотеста'),
        ('5', 'Возможный дефект продукта'),
    ]

    name = models.CharField(max_length=60)
    url_report = models.URLField(blank=True, null=True)
    platform_name = models.CharField(
        max_length=20,
        choices=PLATFORMS,
        default='1'
    )
    build_number = models.IntegerField()
    bug = models.CharField(max_length=30, choices=BUG, default=1)
    floating_defect = models.BooleanField(default=False)
    id_tfs = models.IntegerField(default=1)
    problem = models.TextField()
    my_solution = models.TextField()
    date_create = models.DateField(auto_now_add=True)
