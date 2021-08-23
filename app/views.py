from django.shortcuts import render
import csv

from django.conf import settings

def inflation_view(request):
    template_name = 'app/inflation.html'

    with open('inflation_russia.csv', newline='', encoding='UTF-8') as f:
        content = csv.reader(f, delimiter=';')
        data = list(content)

        return render(request, template_name, {'headers': data[0], 'data': data[1:]})

class User():
    def __init__(self, name):
        self.name = name
    def upper_name(self):
        return self.name.upper()

def test_view(request):

    u = User("Sergey")
    return render(request,'app/test.html', context={'user': u})