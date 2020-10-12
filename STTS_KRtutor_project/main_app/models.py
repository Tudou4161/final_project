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

class ChapterNumberDB(models.Model):  #챕터 넘버링
    Chap_No = models.IntegerField()

class EssentialSentenceDB(models.Model): #필수문장 적재
    Chap_No = models.ForeignKey(ChapterNumberDB.Chap_No, related_name="essential_sentence", on_delete=models.CASCADE)
    Essentence_question = models.CharField(max_length=300)

class ConversationPracticeQuestionDB(models.Model): #발화실습 문장(TTS) 데이터 적재
    Chap_No = models.ForeignKey(ChapterNumberDB.Chap_No, related_name="conversation_question", on_delete=models.CASCADE)
    Cosentence_question = models.CharField(max_length=300)

class ConversationPracticeAnswerDB(models.Model): #발화실습 답변(STT) 데이터 적재
    Chap_No = models.ForeignKey(ChapterNumberDB.Chap_No, related_name="conversation_answer", on_delete=models.CASCADE)
    Cosentence_answer = models.CharField(max_length=300)