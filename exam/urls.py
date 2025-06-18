from django.urls import path
from .views import SubjectList, ChapterList, QuestionList

urlpatterns = [
    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('chapters/<int:subject_id>/', ChapterList.as_view(), name='chapter-list'),
    path('questions/<int:chapter_id>/', QuestionList.as_view(), name='question-list'),
]
