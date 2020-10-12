from django.contrib import admin
from .models import CheckProcess, ConversationPracticeAnswerDB, ConversationPracticeQuestionDB, EssentialSentenceDB

admin.site.register(CheckProcess)
admin.site.register(EssentialSentenceDB)
admin.site.register(ConversationPracticeAnswerDB)
admin.site.register(ConversationPracticeQuestionDB)
