from django.db import models

# Create your models here.
from django.db import models


class ScienceQuestion(models.Model):
    question_text = models.CharField(max_length=300)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100) # Yahan wahi text likhna jo sahi option ka ho

    def __str__(self):
        return self.question_text