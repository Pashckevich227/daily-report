from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from text_report.forms import ReportForm
from .models import Report


def index_view(request):
    report_form = ReportForm()

    distinct_dates = Report.objects.values('date_create').distinct()

    data_for_template = {}
    for date in distinct_dates:
        date_value = date['date_create']
        reports_for_date = Report.objects.filter(date_create=date_value)
        data_for_template[date_value] = reports_for_date

    return render(
        request,
        'index.html',
        {'form': report_form,
         'data_for_template': data_for_template
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
