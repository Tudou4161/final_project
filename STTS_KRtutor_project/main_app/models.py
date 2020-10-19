from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 방법1 : 0 -> 미수료 / 1 -> 수료상태

# 방법2 : null -> 2잠금 / 1 -> 다 열림
# update 함수를 짠다.

class CheckProcess(models.Model):
    user = models.ForeignKey(User, related_name="checkprocess", on_delete=models.CASCADE)
    chap_1 = models.IntegerField(default=1)
    chap_2 = models.IntegerField(default=1)
    chap_3 = models.IntegerField(default=1)
    chap_4 = models.IntegerField(default=1)
    chap_5 = models.IntegerField(default=1)
    chap_6 = models.IntegerField(default=1)
    # def __str__(self):
    #     return f"{self.user.get_username()}"


class ChapterNumberDB(models.Model):  #챕터 넘버링
    ChapNo = models.IntegerField()
    InnerChapOne = models.IntegerField(default=1)
    InnerChapTwo = models.IntegerField(default=2)


class EssentialSentenceDB(models.Model): #필수문장 적재
    #Chap_No = models.ForeignKey(ChapterNumberDB, related_name="essential_sentence", on_delete=models.CASCADE)
    #InnerChapOne = models.ForeignKey(ChapterNumberDB, related_name="essential_sentence1", on_delete=models.CASCADE)
    ChapNo = models.IntegerField()
    #InnerChapOne = models.IntegerField(default=1)
    #InnerChapTwo = models.IntegerField(default=2)
    Essentence_question = models.CharField(max_length=300)


class ConversationPracticeQuestionDB(models.Model): #발화실습 문장(TTS) 데이터 적재
    #Chap_No = models.ForeignKey(ChapterNumberDB, related_name="conversation_question", on_delete=models.CASCADE)
    #InnerChapTwo = models.ForeignKey(ChapterNumberDB, related_name="conversation_question1", on_delete=models.CASCADE)
    ChapNo = models.IntegerField()
    #InnerChapOne = models.IntegerField(default=1)
    #InnerChapTwo = models.IntegerField(default=2)
    Cosentence_question = models.CharField(max_length=300)


class ConversationPracticeAnswerDB(models.Model): #발화실습 답변(STT) 데이터 적재
    ChapNo = models.IntegerField()
    #Chap_No = models.ForeignKey(ChapterNumberDB, related_name="conversation_answer", on_delete=models.CASCADE)
    #InnerChapTwo = models.ForeignKey(ChapterNumberDB, related_name="conversation_answer1", on_delete=models.CASCADE)
    Cosentence_answer = models.CharField(max_length=300)