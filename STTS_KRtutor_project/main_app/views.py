from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
#페이지 네이터 모듈 추가
from django.core.paginator import Paginator
from .models import CheckProcess
from .models import EssentialSentenceDB, ConversationPracticeQuestionDB, ConversationPracticeAnswerDB
from .models import ChapterNumberDB
import json
import os
import sys
import urllib.request

# Create your views here.
def main(request): #로그인 구현 함수
    context = {}

    global en 

    if request.method == "POST":
        en = request.POST["trans_lang_option"]    

    if request.method == "POST":
        if (request.POST["userid"] and request.POST["password"]):
            
            user = auth.authenticate(
                request,
                username=request.POST["userid"],
                password=request.POST["password"]
            )

            if user is not None:
                auth.login(request, user)
                chap_no = ChapterNumberDB.objects.all()
                #로그인과 동시에 메인화면을 보여줘야함. 여기서 문제가 발생해서 수정함.
                context = {
                    'chap_number' : chap_no
                }

                return render(request, "chapter.html", context)
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
    chap_no = ChapterNumberDB.objects.all()

    context = {
        'chap_number' : chap_no,
    }

    return render(request, "chapter.html", context)


def chap_detail(request, cn_ChapNo):
    chap_detail = ChapterNumberDB.objects.get(ChapNo=cn_ChapNo)
    #chapter_Number를 전역변수에 담아준다.
    global chap_number
    chap_number = cn_ChapNo

    
    context = {
        'chap_detail' : chap_detail,
    }

    return render(request, 'chap_detail.html', context)


def chap_sentence_ES(request):
    sentence_list = EssentialSentenceDB.objects.filter(ChapNo=chap_number,InnerNo=1)

    trans_list = []
    for idx in range(len(sentence_list)):
        page = request.GET.get('page')
        if page == None:
            page = 1
            if idx == page-1:
                trans_stc = translate(sentence_list.values()[idx]["Essentence_question"], en)
                trans_list.append(trans_stc)
        else:
            page = int(page)
            if idx == page-1:
                trans_stc = translate(sentence_list.values()[idx]["Essentence_question"], en)
                trans_list.append(trans_stc)

    # sentence_list = EssentialSentenceDB.objects.all()
    paginator = Paginator(sentence_list, 1)
    paginator_trans = Paginator(trans_list, 1)

    page = request.GET.get('page')

    sentences = paginator.get_page(page)
    sentences_trans = paginator_trans.get_page(page)

    if request.method == "POST":
        if "sendtext" in request.POST:
            sendtext = request.POST["sendtext"]
            origintext = request.POST["origintext"]
            print(origintext)
            print(sendtext)

            sent = (sendtext, origintext)
            
            tfidf_vec = TfidfVectorizer() 
            tfidf_mat = tfidf_vec.fit_transform(sent)
            threshold = cosine_similarity(tfidf_mat[0:1], tfidf_mat[1:2])

            if threshold > 0.3:
                print("맞았습니다.")
            else:
                print("틀렸습니다. 다시 시도해주세요!")

        else:
            sendtext = False

    
    context = {
        "sentences" : sentences,
        "sentences_trans" : sentences_trans
    }

    return render(request, "chap_sentence.html", context)

def chap_sentence_Con(request):
    question_list = ConversationPracticeQuestionDB.objects.filter(ChapNo=chap_number, InnerNo=2)
    answer_list = ConversationPracticeAnswerDB.objects.filter(ChapNo=chap_number, InnerNo=2)

    question_trans_list = []
    for idx in range(len(question_list)):
        page = request.GET.get('page')
        if page == None:
            page = 1
            if idx == page-1:
                question_trans_stc = translate(question_list.values()[idx]["Cosentence_question"], en)
                question_trans_list.append(question_trans_stc)
        else:
            page = int(page)
            if idx == page-1:
                question_trans_stc = translate(question_list.values()[idx]["Cosentence_question"], en)
                question_trans_list.append(question_trans_stc)

    answer_trans_list = []
    for idx in range(len(answer_list)):
        page = request.GET.get('page')
        if page == None:
            page = 1
            if idx == page-1:
                answer_trans_stc = translate(answer_list.values()[idx]["Cosentence_answer"], en)
                answer_trans_list.append(answer_trans_stc)
        else:
            page = int(page)
            if idx == page-1:
                answer_trans_stc = translate(answer_list.values()[idx]["Cosentence_answer"], en)
                answer_trans_list.append(answer_trans_stc)

    paginator_q = Paginator(question_list, 1)
    paginator_q_trans = Paginator(question_trans_list, 1)
    paginator_a = Paginator(answer_list, 1)
    paginator_a_trans = Paginator(answer_trans_list, 1)

    page = request.GET.get('page')

    question = paginator_q.get_page(page)
    question_trans = paginator_q_trans.get_page(page)
    answer = paginator_a.get_page(page)
    answer_trans = paginator_a_trans.get_page(page)

    if request.method == "POST":
        if "sendtext" in request.POST:
            sendtext = request.POST["sendtext"]
            origintext = request.POST["origintext"]
            print(origintext)
            print(sendtext)

            sent = (sendtext, origintext)
            
            tfidf_vec = TfidfVectorizer() 
            tfidf_mat = tfidf_vec.fit_transform(sent)
            threshold = cosine_similarity(tfidf_mat[0:1], tfidf_mat[1:2])

            if threshold > 0.3:
                print("맞았습니다.")
            else:
                print("틀렸습니다. 다시 시도해주세요!")

        else:
            sendtext = False

    context = {
        "question" : question,
        "question_trans" : question_trans,
        "answer" : answer,
        "answer_trans" : answer_trans
    }

    return render(request, "chap_sentence2.html", context)
    

    
def LV1clear(request):
    return render(request, "LV1clear.html")


def translate(sentence, target_lang):
    client_id = "deribthgxo"
    client_secret = "8NOoY9KhtwKHKZwpOQYr5bovSKA6DSctcC9eClf8"
    encText = urllib.parse.quote(sentence)
    data = f"source=ko&target={target_lang}&text=" + encText

    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        result = response_body.decode('utf-8')
        json_sentence = json.loads(result)
        return json_sentence["message"]["result"]["translatedText"]
        
    else:
        return "Error Code:" + rescode























#import csv
# csv_path = r"C:\Users\WIN10\Desktop\final_project\final_project\STTS_KRtutor_project\main_app\data\Essential_sentence.csv"
# # sentence 데이터베이스 저장하기
# # 아래 파일들은 주석을 하나씩 해제해서, 집어넣어야함.
# # 그렇게 안하면, 매우 큰 문제가 발생합니다.....^^
# with open(csv_path, 'r', encoding='utf-8') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         print(row)
#         EssentialSentenceDB.objects.create(
#             ChapNo=row["chap_no"],
#             InnerNo=row["inner_no"],
#             SentenceNo=row["sentence_no"],
#             Essentence_question=row["sentence"]
#         )

# csv_path = r"C:\Users\WIN10\Desktop\final_project\final_project\STTS_KRtutor_project\main_app\data\answer_sentence.csv"
# # sentence 데이터베이스 저장하기
# with open(csv_path, 'r', encoding='utf-8') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         print(row)
#         ConversationPracticeAnswerDB.objects.create(
#             ChapNo=row["chap_no"],
#             InnerNo=row["inner_no"],
#             SentenceNo=row["sentence_no"],     
#             Cosentence_answer=row["sentence"]
#         )

# csv_path = r"C:\Users\WIN10\Desktop\final_project\final_project\STTS_KRtutor_project\main_app\data\TTS_sentence.csv"
# # sentence 데이터베이스 저장하기
# with open(csv_path, 'r', encoding='utf-8') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         print(row)
#         ConversationPracticeQuestionDB.objects.create(
#             ChapNo=row["chap_no"],
#             InnerNo=row["inner_no"],
#             SentenceNo=row["sentence_no"],
#             Cosentence_question=row["sentence"]
#         )