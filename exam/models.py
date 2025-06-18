from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='chapters')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject.name} - {self.name}"


class Question(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)  # Store the correct answer text

    def __str__(self):
        return self.question_text[:50]
