from django import template

register = template.Library()



@register.filter()
def format_empty_value(value):
        if not value:
            return "-"
        return value

@register.filter()
def rows_format(value):
    if value:
        val = float(value)
        if val < 0:
            return '#36C42A'
        elif 1 < val <= 2:
            return '#F99A86'
        elif 2 < val <= 5:
            return '#E65C3F'
        elif 5 < val:
            return '#C92B0A'
        elif value == "-":
            return '#FFFFFF'
        else:
            return '#FFFFFF'
    return '-'
