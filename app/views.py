from django.shortcuts import render
import csv

from django.conf import settings

def inflation_view(request):
    template_name = 'app/inflation.html'

    with open('inflation_russia.csv', newline='', encoding='UTF-8') as f:
        content = csv.reader(f, delimiter=';')
        data = list(content)

        return render(request, template_name, {'headers': data[0], 'data': data[1:]})

