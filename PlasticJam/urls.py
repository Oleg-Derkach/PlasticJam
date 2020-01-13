from django.urls import path
from .views import list_view, user_page

app_name = 'PlasticJam'

urlpatterns = [
    path('', list_view, name='list_view'),
    path('user_page/<ids>/', user_page, name='user_page'),
    
] 