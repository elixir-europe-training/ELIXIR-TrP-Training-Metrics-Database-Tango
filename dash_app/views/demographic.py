from .common import get_tabs
from django.shortcuts import render


def demographic_report(request):
    return render(
        request,
        'dash_app/template.html',
        context={
            **get_tabs(request)
        }
    )