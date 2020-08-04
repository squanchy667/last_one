
from rest_framework import viewsets
from .models import Employer, CONtacts
from .serializers import EMployerserializer, COntactsserializer
from django.http import HttpResponse
import xlwt
from calendar import monthrange



class EmployerView(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EMployerserializer


class ContactsView(viewsets.ModelViewSet):
    queryset = CONtacts.objects.all()
    serializer_class = COntactsserializer


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('employer')
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Username', 'identifier', 'phone', 'email', 'contacts', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = Employer.objects.all().values_list('name', 'identifier', 'phone', 'email', 'contacts', )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response


def last_day_of_month(request, y, m):
    result = monthrange(y, m)
    return HttpResponse('<h1> the Last day of the month is {}<h1>'.format(result[1]))

