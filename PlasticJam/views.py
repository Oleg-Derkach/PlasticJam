from django.shortcuts import render, render_to_response
from .models import Statistic, User, Statistic_Block
from django.core.paginator import Paginator
from chartit import DataPool, Chart

def is_valid_queryparam(param):
    return param != '' and param is not None


def list_view(request):
    
    static_block = Statistic_Block.objects.all()
    paginator = Paginator(static_block, 50) 
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    is_paginated = queryset.has_other_pages()
  
    response = render(request, "index.html", 
        {'query_products':queryset,
         'is_paginated':is_paginated,}) 

    return response 
 

def user_page(request, ids):

    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')   
    
    stat = Statistic.objects.filter(user=ids)
    
    if is_valid_queryparam(date_min):
        stat = stat.filter(date__gte=date_min)

    if is_valid_queryparam(date_max):
        stat = stat.filter(date__lte=date_max)
        
    weatherdata = DataPool(series= [{'options': {'source': stat},
                                     'terms': ['date','page_views','clicks']}])
    chart = Chart(datasource = weatherdata, series_options = [{'options':{
                  'type': 'line', 'stacking': False},'terms':{'date': [
            'page_views','clicks']}}],
            chart_options = {'title': {'text': 'Statistic'},
               'xAxis': {'title': { 'text': 'Day'}}})

    return render_to_response('user_page.html', {'statistic_chart': chart,
                                                 'stat_user':stat[0]})  



















