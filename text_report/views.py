import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from text_report.forms import ReportForm
from .models import Report


def index_view(request):
    report_form = ReportForm()

    today = datetime.date.today()
    reports_today = Report.objects.filter(date_create=today)
    reports_after = Report.objects.exclude(date_create=today)

    return render(
        request,
        'index.html',
        {'form': report_form,
         'reports_after': reports_after,
         'reports_today': reports_today
         })


def report_view(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            floating_bug_value = 'floating_bug' in request.POST

            name = request.POST["name"]
            url_report = request.POST["url_report"]
            platform_name = request.POST["platform_name"]
            build_number = request.POST["build_number"]
            bug = request.POST["bug"]
            id_tfs = request.POST["id_tfs"]
            problem = request.POST["problem"]
            my_solution = request.POST["my_solution"]

            new_report = Report(name=name,
                                url_report=url_report,
                                platform_name=platform_name,
                                build_number=build_number,
                                bug=bug,
                                floating_defect=floating_bug_value,
                                id_tfs=id_tfs,
                                problem=problem,
                                my_solution=my_solution)
            new_report.save()
            return HttpResponseRedirect(reverse('index_view'))
    else:
        form = ReportForm()

    return render(request, 'index.html', {'form': form})


def history_view(request):
    reports = Report.objects.all()
    context = {'reports': reports}
    return render(request, 'index.html', context)
