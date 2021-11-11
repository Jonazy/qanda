from django.urls import path
from qa.views import (QuestionView, QuestionDetailView, QuestionListView, CreateAnswerView)

app_name = 'qa'
urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='questions'),
    path('question/', QuestionView.as_view(), name='add-question'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question'),
    path('question/<int:pk>/answer/', CreateAnswerView.as_view(), name='add-answer'),
]
