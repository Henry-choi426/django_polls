from django.urls import path

# View모듈 import
from . import views
from django.views.generic import ListView, DetailView
from .models import Question, Choice

# 요청url - 함수 매핑 => urlpatterns 변수의 리스트에 등록
app_name = 'poll'
urlpatterns = [ 
    path("list/", views.QuestionListView.as_view(), name='list'),  #poll/list => QuestionListView 호출
    # path("list/", ListView.as_view(model=Question, template_name='poll/list.html'), name = 'list'),
    path("vote/<int:question_id>", views.VoteView.as_view(), name='vote'),  #poll/vote_form => view.vote_form 함수 호출
    path('my_vote_result/<int:pk>', views.QuestionDetailView.as_view(), name='vote_result')
    # path("my_vote_result/<int:pk>", DetailView.as_view(model=Question, template_name='poll/vote_result.html'), name = 'vote_result'),

]




# 사용자 요청 url - http://ip:port/resource_path
# config.urls.py 에 등록: resource_path
# resource_path: app_root/나머지_path
# config/urls.py : app_root/(poll/) => poll/urls.py 에서 나머지_path를 확인
# polls/urls.py  : 나머지_path => view함수를 mapping

