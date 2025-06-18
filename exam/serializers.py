from rest_framework import serializers
from .models import Subject, Chapter, Question

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'name', 'subject']


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'options', 'answer']

    def get_options(self, obj):
        return [obj.option1, obj.option2, obj.option3, obj.option4]
