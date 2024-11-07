from django.urls import path
from .views import report_view, history_view, index_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('form/', report_view, name='text_report'),
    path('history/', history_view, name='history_view')
]
