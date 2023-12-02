from .models import Report
from django import forms


class ReportForm(forms.Form):
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

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Сценарий',
        'type': 'text'
    }))

    url_report = forms.URLField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'URL сценария',
        'type': 'url'
    }))

    platform_name = forms.ChoiceField(choices=PLATFORMS, widget=forms.Select(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Платформа',
    }))

    build_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Сборка',
        'type': 'text'
    }))

    problem = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Проблема',
        'type': 'text'
    }))

    my_solution = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Мое решение',
        'type': 'text'
    }))

    class Meta:
        model = Report
        fields = ('name', 'url_report', 'platform_name', 'build_number', 'problem', 'my_solution')