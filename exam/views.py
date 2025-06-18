from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Subject, Chapter, Question
from rest_framework.permissions import AllowAny
from .serializers import SubjectSerializer, ChapterSerializer, QuestionSerializer

class SubjectList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        permission_classes = [AllowAny] 
        return Response(serializer.data)


class ChapterList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, subject_id):
        chapters = Chapter.objects.filter(subject_id=subject_id)
        serializer = ChapterSerializer(chapters, many=True)
        
        return Response(serializer.data)


class QuestionList(APIView):
    permission_classes = [AllowAny] 

    def get(self, request, chapter_id):
        questions = Question.objects.filter(chapter_id=chapter_id)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
