from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

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
            
            new_user = User.objects.create_user(
                username=request.POST["userid"],
                password=request.POST["password"]
            )

            auth.login(request, new_user)
            return render(request, "chapter.html")

        else:
            context["error"] = "아이디와 비밀번호를 다시 확인해주세요"
    return render(request, "sign_up.html", context)

def chapter(request):
    return render(request, "chapter.html")