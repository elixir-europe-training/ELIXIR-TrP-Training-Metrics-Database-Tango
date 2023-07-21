from datetime import datetime
from functools import lru_cache
from contextlib import suppress
from .models import Event, Quality, Impact, Demographic


class EventGroup():
    def __init__(
        self,
        name,
        field_mapping,
        use_fields=None,
        filter_fields=[
            "type",
            "funding",
            "target_audience",
            "additional_platforms"
        ],
        graph_type="bar"
    ):
        self.field_mapping = field_mapping
        self.name = name
        self.filter_fields = filter_fields
        self.graph_type = graph_type
        self.model = Event
        self.use_fields = use_fields
        self.fields = {
            field_id: self.model.objects.order_by().values(field_id).distinct().values_list(field_id, flat=True)
            for field_id in self.use_fields
        }
        
    
    def get_graph_type(self):
        return self.graph_type

    def get_fields(self):
        return self.use_fields
    
    def get_filter_fields(self):
        return self.filter_fields
    
    def get_field_placeholder(self, field_id):
        return f"Select {self.get_field_title(field_id)}"
    
    def get_field_options(self, field_id):
        return self.fields[field_id]
    
    def get_field_title(self, lookup_id):
        for name, field_id in self.field_mapping.items():
            if lookup_id == field_id:
                return name
        return lookup_id
        
    
    def get_values(self, **params):
        query = self.model.objects.all()
        if params.get("type"):
            query = query.filter(type=params.get("type"))
        if params.get("funding"):
            query = query.filter(funding=params.get("funding"))
        if params.get("target_audience"):
            query = query.filter(target_audience=params.get("target_audience"))
        if params.get("additional_platforms"):
            query = query.filter(additional_platforms=params.get("additional_platforms"))

        date_from = params.get("date_from")
        date_to = params.get("date_to")
        if date_from is not None and date_to is not None:
            query = query.filter(date_start__range=[date_from, date_to]).filter(date_end__range=[date_from, date_to])
        if params.get("node_only"):
            pass
        
        result = list(query.values())
        return result
    
    def get_name(self):
        return self.name


class Group():
    def __init__(
        self,
        name,
        field_mapping,
        model,
        use_fields=None,
        filter_fields=[
            "event_type",
            "event_funding",
            "event_target_audience",
            "event_additional_platforms"
        ],
        graph_type="bar"
    ):
        self.field_mapping = field_mapping
        self.name = name
        self.filter_fields = filter_fields
        self.graph_type = graph_type
        self.model = model
        self.use_fields = use_fields
        self.fields = {
            **{
                field_id: self.model.objects.order_by().values(field_id).distinct().values_list(field_id, flat=True)
                for field_id in self.use_fields
            },
            **{
                f"event_{field_id}": Event.objects.order_by().values(field_id).distinct().values_list(field_id, flat=True)
                for field_id in [
                    "type",
                    "funding",
                    "target_audience",
                    "additional_platforms",
                    "communities",
                ]
            }
        }
        
    
    def get_graph_type(self):
        return self.graph_type

    def get_fields(self):
        return self.use_fields
    
    def get_filter_fields(self):
        return self.filter_fields
    
    def get_field_placeholder(self, field_id):
        return f"Select {self.get_field_title(field_id)}"
    
    def get_field_options(self, field_id):
        return self.fields[field_id]
    
    def get_field_title(self, lookup_id):
        for name, field_id in self.field_mapping.items():
            if lookup_id == field_id:
                return name
        return lookup_id
        
    
    def get_values(self, **params):
        query = self.model.objects.all()
        if params.get("event_type"):
            query = query.filter(event__type=params.get("event_type"))
        if params.get("event_funding"):
            query = query.filter(event__funding=params.get("event_funding"))
        if params.get("event_target_audience"):
            query = query.filter(event__target_audience=params.get("event_target_audience"))
        if params.get("event_additional_platforms"):
            query = query.filter(event__additional_platforms=params.get("event_additional_platforms"))

        date_from = params.get("date_from")
        date_to = params.get("date_to")
        if date_from is not None and date_to is not None:
            query = query.filter(event__date_start__range=[date_from, date_to]).filter(event__date_end__range=[date_from, date_to])
        if params.get("node_only"):
            pass
        
        result = list(query.values())
        return result
    
    def get_name(self):
        return self.name


class Metrics():
    def __init__(self, groups):
        self.groups = groups

    def get_group(self, name):
        return self.groups.get(name, None)


@lru_cache
def get_metrics():
    groups = {
        "event": EventGroup(
            "Number of answers",
            {},
            use_fields=[
                "type",
                "funding",
                "target_audience",
                "additional_platforms"
            ]
        ),
        "impact": Group(
            "Number of answers",
            {},
            Impact,
            use_fields=[
                "when_attend_training",
                "main_attend_reason",
                "how_often_use_before",
                "how_often_use_after",
                "able_to_explain",
                "able_use_now",
                "attending_led_to",
                "people_share_knowledge",
                "recommend_others",
            ],
            graph_type="pie"
        ),
        "quality": Group(
            "Number of answers",
            {},
            Quality,
            use_fields=[
                "used_resources_before",
                "used_resources_future",
                "recommend_course",
                "course_rating",
                "balance",
                "email_contact",
            ],
            graph_type="pie"
        ),
        "demographic": Group(
            "Number of answers",
            {},
            Demographic,
            use_fields=[
                "employment_country",
                "heard_from",
                "employment_sector",
                "gender",
                "career_stage",
            ],
            graph_type="pie"
        ),
    }
    return Metrics(groups)

def metrics_middleware(get_response):
    def middleware(request):
        setattr(request, "metrics", get_metrics())
        response = get_response(request)
        return response

    return middleware