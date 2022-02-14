from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))

LIST_STATION = []
with open('data-398-2018-08-30.csv', encoding='utf-8') as csvfile:
    data = csv.reader(csvfile)
    headers = next(data)
    for row in data:
        dict_temp = {
            'Name': row[1],
            'Street': row[4],
            'District': row[6]
        }
        LIST_STATION.append(dict_temp)


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(LIST_STATION, 10)
    bus_stations = paginator.get_page(page_number)
    page = paginator.page(page_number)

    context = {
        'bus_stations': bus_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
