from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import CheckProcess

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