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


# def chap_sentence_ES(request):
#     if request.method == "POST": #만약 templates 메소드가 POST이면..
#         if 'kor_stt_sentence' in request.POST:
#             user_post_sentence = request.GET["kor_stt_sentence"] #사용자가 말한 문장을 변수에 저장하고, 아래의 과정에 따라 유사도를 측정한다.
#             sent = (user_post_sentence,
#                     search.values()[cnt]['Essentence_question'])
            
#             tfidf_vec = TfidfVectorizer() 
#             tfidf_mat = tfidf_vec.fit_transform(sent)
#             threshold = cosine_similarity(tfidf_mat[0:1], tfidf_mat[1:2])

#             if threshold > 0.3: #임계치가 0.3을 넘으면...
#                 cnt += 1 #cnt를 증가시켜준다.
#                 if_alert = "맞았습니다. 다음 문장으로 넘어가주세요"
#                 if_context = {
#                     'if_alert' : if_alert,
#                     'sentence' : search.get(SentenceNo=cnt)
#                 }
#                 return render(request, "chap_sentence.html", if_context)

#             elif threshold <= 0.3:
#                 elif_alert = "틀렸습니다. 다시 말씀해주세요."
#                 elif_context = {
#                     'elif_alert' : elif_alert,
#                     'sentence' : search.get(SentenceNo=cnt)
#                 }
#                 return render(request, "chap_sentence.html", elif_context)


def chap_sentence_ES(request):
    #sentence_list = EssentialSentenceDB.objects.filter(ChapNo=chap_number,InnerNo=1)

    sentence_list = EssentialSentenceDB.objects.all()
    paginator = Paginator(sentence_list, 1)

    page = request.GET.get('page')

    sentences = paginator.get_page(page)

    return render(request, "chap_sentence.html", {"sentences" : sentences})



def chap_sentence_Con(request):
    inner_no = request.POST["lv2"]

    search1 = ConversationPracticeQuestionDB.objects.filter(ChapNo=chap_number, InnerNo=int(inner_no))
    search2 = ConversationPracticeAnswerDB.objects.filter(ChapNo=chap_number, InnerNo=int(inner_no))

    context = {
        'question' : search1,
        'answer' : search2
    }

    return render(request, "chap_sentence2.html", context)
    
    
def LV1clear(request):
    return render(request, "LV1clear.html")


























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