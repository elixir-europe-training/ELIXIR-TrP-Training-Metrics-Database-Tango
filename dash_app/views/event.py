from .common import get_layout, use_callback, get_tabs

from django_plotly_dash import DjangoDash
from django.shortcuts import render

app = DjangoDash("EventReport")

def event_report(request):
    group = request.metrics.get_group('event')
    dash_config = {}
    if group:
        app.layout = get_layout(app, group)
        use_callback(app, group)
        dash_config = {
            "dash_name": "EventReport"
        }

    return render(
        request,
        'dash_app/template.html',
        context={
            **get_tabs(request),
            **dash_config
        }
    )


