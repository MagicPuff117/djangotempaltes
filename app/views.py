from django.shortcuts import render
import csv



def inflation_view(request):
    template_name = 'app/inflation.html'

    with open('inflation_russia.csv', encoding='UTF-8') as f:
        content = csv.reader(f, delimiter=';')
        rows1 =[]
        for lines in content:
            rows2 = []
            for row in lines:
                if row:
                    rows2.append(row)
                else:
                    rows2.append('-')
            rows1.append(rows2)
        context = {'header': rows1[0],'data': rows1[1:]}

        return render(request, template_name, context)


def test_view(request):
    template_name = 'app/data.html'
    context = {'username':'Vova'}

    return render(request, template_name, context)