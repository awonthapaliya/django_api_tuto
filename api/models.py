# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class QuestionAnswer(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    
def __str__(self):
    return '%s %s' % (self.question, self.answer) 