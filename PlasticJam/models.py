from django.db import models
from django.shortcuts import reverse

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    ip_address = models.CharField(max_length=20)
    
    def get_absolute_url(self):
        return reverse("PlasticJam:user_page", kwargs={'ids': self.id})
    
    

class Statistic(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField()
    page_views = models.IntegerField()
    clicks = models.IntegerField()
    
#{'user_id': 10, 
# 'date': '2019-10-15', 
# 'page_views': 938, 
# 'clicks': 887}


class Statistic_Block(models.Model):
    user = models.OneToOneField(User,primary_key=True,
                                on_delete=models.CASCADE)
    statistic = models.ManyToManyField(Statistic)

    def total_clicks(self):
        total = 0
        statistic_block = self.statistic.filter(user=self.user)
        for cl in statistic_block:
            total += cl.clicks
        return total
         
    def total_page_views(self):
        total = 0
        statistic_block = self.statistic.filter(user=self.user)
        for cl in statistic_block:
            total += cl.page_views
        return total
    






