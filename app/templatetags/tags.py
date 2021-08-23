from django import template

register = template.Library()



@register.filter()
def format_empty_value(value):
        if not value:
            return "-"
        return value