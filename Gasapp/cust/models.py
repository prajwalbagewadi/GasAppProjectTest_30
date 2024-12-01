from django.db import models

# Create your models here.
class CustReq(models.Model):
    usid=models.IntegerField(default=0)
    user=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)
    add=models.TextField()
    issue=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)
    stat=models.CharField(max_length=20,default='open')
    reqid=models.IntegerField(default=0)
    
class Meta:
    app_label = 'cust'  # Explicitly add the app_label here
    