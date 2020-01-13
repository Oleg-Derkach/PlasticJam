
import json



#[{'id': 1, 
#  'first_name': 'Christie', 
#  'last_name': 'Gann', 
#  'email': 'cgann0@hostgator.com', 
#  'gender': 'Female', 
#  'ip_address': '57.14.195.231'}, {'id': 2, 'first_name': 'Hamil', 'last_name': 'Cressey', 'email': 'hcressey1@delicious.com', 'gender': 'Male', 'ip_address': '45.225.25.145'}, {'id': 3, 'first_name': 'Lottie', 'last_name': 'Dupre', 'email': 'ldupre2@dot.gov', 'gender': 'Female', 'ip_address': '254.46.181.79'}, {'id': 4, 'first_name': 'Godfry', 'last_name': 'Raoult', 

import xlrd
import os, sys


PROJECT_DIR = os.getcwd() + '\\Main'
sys.path.append(PROJECT_DIR)
os.environ["DJANGO_SETTINGS_MODULE"] = 'settings'

import django

django.setup()

from PlasticJam.models import User, Statistic, Statistic_Block


with open("users.json", "r") as read_file:
    data = json.load(read_file)
    
with open("users_statistic.json", "r") as read_file:
    static = json.load(read_file)    

#{'id': 1, 
#  'first_name': 'Christie', 
#  'last_name': 'Gann', 
#  'email': 'cgann0@hostgator.com', 
#  'gender': 'Female', 
#  'ip_address': '57.14.195.231'}

#data = data[:10]
#static = static[:20]

for item in data:

    user = User()
    user.id = item['id'] 
    user.first_name = item['first_name'] 
    user.last_name = item['last_name']
    user.email = item['email'] 
    user.gender = item['gender']
    user.ip_address = item['ip_address']
    user.save()
    print(user.id)
#    
##{'user_id': 10, 
## 'date': '2019-10-15', 
## 'page_views': 938, 
## 'clicks': 887}
#    
    s = Statistic_Block.objects.create(user=user)
    for st in static:
        if st['user_id'] == item['id']:
            stat = Statistic()
            stat.user = user
            stat.date = st['date']
            stat.page_views = st['page_views']
            stat.clicks = st['clicks']
            stat.save()  
            
            s.statistic.add(stat)
            s.save()
# 
#    
    
    
#sta = Statistic.objects.create(
#        user = user,
#        date = '2019-04-05',
#        page_views = 1324,
#        clicks = 1142 )
    
    
    
    
    
    
    
    
