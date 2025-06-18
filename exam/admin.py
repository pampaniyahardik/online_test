from django.contrib import admin
from .models import Subject, Chapter, Question

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_filter = ['subject']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'chapter', 'answer']
    list_filter = ['chapter']
