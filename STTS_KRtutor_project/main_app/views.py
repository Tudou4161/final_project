from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import CheckProcess
from .models import EssentialSentenceDB, ConversationPracticeQuestionDB, ConversationPracticeAnswerDB
import csv

# Create your views here.
def main(request): #로그인 구현 함수
    context = {}
    if request.method == "POST":
        if (request.POST["userid"] and request.POST["password"]):
            
            user = auth.authenticate(
                request,
                username=request.POST["userid"],
                password=request.POST["password"]
            )

            if user is not None:
                auth.login(request, user)
                return render(request, "chapter.html")
            else:
                context["error"] = "아이디와 비밀번호를 다시 확인해주세요."
        else:
            context["error"] = "아이디와 비밀번호를 다시 확인해주세요."

    return render(request, "main.html", context)


def sign_up(request): #회원가입 구현함수
    context = {}
    if request.method == "POST":
        if (request.POST["userid"] and request.POST["password"] and
                request.POST["password"] == request.POST["password_check"]):

            user_id = request.POST["userid"]

            new_user = User.objects.create_user(
                username=user_id,
                password=request.POST["password"]
            )

            new_CheckTable = CheckProcess(
                user=User.objects.get(username=user_id),
                chap_1= 1,
                chap_2= 1,
                chap_3= 1,
                chap_4= 1,
                chap_5= 1,
                chap_6= 1
            )
            new_CheckTable.save()

            auth.login(request, new_user)
            return redirect("main")

        else:
            context["error"] = "아이디와 비밀번호 를 다시 입력해주세요"

    return render(request, "sign_up.html", context)

def logout(request):
    if request.method == "POST":
        auth.logout(request)
    return redirect("main")


def chapter(request):
    return render(request, "chapter.html")

def chap1(request):
    return render(request, "chap1.html")


























# csv_path = r"C:\Users\WIN10\Desktop\final_project\final_project\STTS_KRtutor_project\main_app\data\Essential_sentence.csv"
# # sentence 데이터베이스 저장하기
# # 아래 파일들은 주석을 하나씩 해제해서, 집어넣어야함.
# # 그렇게 안하면, 매우 큰 문제가 발생합니다.....^^
# with open(csv_path, 'r', encoding='utf-8') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         print(row)
#         EssentialSentenceDB.objects.create(
#             Chap_No=row["chap_no"],
#             Essentence_question=row["sentence"]
#         )

# csv_path = r"C:\Users\WIN10\Desktop\final_project\final_project\STTS_KRtutor_project\main_app\data\answer_sentence.csv"
# # sentence 데이터베이스 저장하기
# with open(csv_path, 'r', encoding='utf-8') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         print(row)
#         ConversationPracticeAnswerDB.objects.create(
#             Chap_No=row["chap_no"],
#             Cosentence_answer=row["answer"]
#         )

# csv_path = r"C:\Users\WIN10\Desktop\final_project\final_project\STTS_KRtutor_project\main_app\data\TTS_sentence.csv"
# # sentence 데이터베이스 저장하기
# with open(csv_path, 'r', encoding='utf-8') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         print(row)
#         ConversationPracticeQuestionDB.objects.create(
#             Chap_No=row["chap_no"],
#             Cosentence_question=row["question"]
#         )