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
    path('chap_detail/<int:cn_ChapNo>', views.chap_detail, name="chap_detail"),
    #path('chap_detail/<int:cn_ChapNo>/chap_sentence/<int:es_sentence_no>', views.chap_Essential_sentence, name="chap_Essential_sentence")
    #path('chap_detail/<int:cn_ChapNo>/chap_sentence/<int:co_sentence_no>', views.chap_Conversation_sentence, name="chap_Conversation_sentence")
]
