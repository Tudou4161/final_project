from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 방법1 : 0 -> 미수료 / 1 -> 수료상태

# 방법2 : null -> 2잠금 / 1 -> 다 열림
# update 함수를 짠다.

class CheckProcess(models.Model):
    user = models.ForeignKey(User, related_name="checkprocess", on_delete=models.CASCADE)
    chap_1 = models.IntegerField()
    chap_2 = models.IntegerField()
    chap_3 = models.IntegerField()
    chap_4 = models.IntegerField()
    chap_5 = models.IntegerField()
    chap_6 = models.IntegerField()

    # def __str__(self):
    #     return f"{self.user.get_username()}"


#일단 주석처리 ...
# class CheckProcessDetailsChap1(models.Model):
#     username = models.ForeignKey(User, related_name="checkprocess", on_delete=models.CASCADE)
#     chap_1_check = models.ForeignKey(CheckProcess.chap_1, related_name="chap_1_checks", on_delete=models.CASCADE)
#     chap_1_1_check = models.IntegerField()
#     chap_1_2_check = models.IntegerField()


# class CheckProcessDetailsChap2(models.Model):
#     username = models.ForeignKey(User, related_name="checkprocess", on_delete=models.CASCADE)
#     chap_2_check = models.ForeignKey('CheckProcess.chap_2', related_name="chap_2_checks", on_delete=models.CASCADE)
#     chap_2_1_check = models.IntegerField()
#     chap_2_2_check = models.IntegerField()


# class CheckProcessDetailsChap3(models.Model):
#     username = models.ForeignKey(User, related_name="checkprocess", on_delete=models.CASCADE)
#     chap_3_check = models.ForeignKey('CheckProcess.chap_3', related_name="chap_3_checks", on_delete=models.CASCADE)
#     chap_3_1_check = models.IntegerField()
#     chap_3_2_check = models.IntegerField()


# class CheckProcessDetailsChap4(models.Model):
#     username = models.ForeignKey(User, related_name="checkprocess", on_delete=models.CASCADE)
#     chap_4_check = models.ForeignKey('CheckProcess.chap_4', related_name="chap_4_checks", on_delete=models.CASCADE)
#     chap_4_1_check = models.IntegerField()
#     chap_4_2_check = models.IntegerField()


# class CheckProcessDetailsChap5(models.Model):
#     username = models.ForeignKey(User, related_name="checkprocess", on_delete=models.CASCADE)
#     chap_5_check = models.ForeignKey('CheckProcess.chap_5', related_name="chap_5_checks", on_delete=models.CASCADE)
#     chap_5_1_check = models.IntegerField()
#     chap_5_2_check = models.IntegerField()


# class CheckProcessDetailsChap6(models.Model):
#     username = models.ForeignKey(User, related_name="checkprocess", on_delete=models.CASCADE)
#     chap_6_check = models.ForeignKey('CheckProcess.chap_6', related_name="chap_6_checks", on_delete=models.CASCADE)
#     chap_6_1_check = models.IntegerField()
#     chap_6_2_check = models.IntegerField()