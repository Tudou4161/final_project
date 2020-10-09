from django.db import models

# Create your models here.

class CheckProcess(models.Model):
    user_id = models.CharField(max_length=300)
    chap_1 = models.IntegerField()
    chap_2 = models.IntegerField()
    chap_3 = models.IntegerField()
    chap_4 = models.IntegerField()
    chap_5 = models.IntegerField()
    chap_6 = models.IntegerField()
    #고객 아이디
    #챕터1
    #챕터2
    #챕터3
    #챕터4
    #챕터5
    #챕터6

class CheckProcessDetailsChap1(models.Model):
    pass;

class CheckProcessDetailsChap2(models.Model):
    pass;

class CheckProcessDetailsChap3(models.Model):
    pass;

class CheckProcessDetailsChap4(models.Model):
    pass;

class CheckProcessDetailsChap5(models.Model):
    pass;

class CheckProcessDetailsChap6(models.Model):
    pass;
    
