from django.db import models


class Exam(models.Model):
    Question  = models.CharField(max_length=100)
    option1  = models.CharField(max_length=100)
    option2  = models.CharField(max_length=100)
    option3  = models.CharField(max_length=100)
    option4  = models.CharField(max_length=100)
    Correct_Answer = models.CharField(max_length=100)

    class Meta:
        db_table = 'onlineexam'