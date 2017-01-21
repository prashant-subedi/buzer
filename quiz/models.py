from django.db import models

# Create your models here.

class QuizModel(models.Model):
	ready=models.BooleanField(default="False")