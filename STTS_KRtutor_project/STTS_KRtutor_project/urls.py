"""STTS_KRtutor_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from main_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('logout/', views.logout, name="logout"),
    path('<int:cn_ChapNo>/chap_detail', views.chap_detail, name="chap_detail"),
    path('chap_sentence/<int:escontent_SentenceNo>', views.chap_sentence_ES, name="chap_Essential_sentence"),
    path('chapter', views.chapter, name="chapter"),
    #path('LV1clear', views.LV1clear, name="LV1clear"),
]
