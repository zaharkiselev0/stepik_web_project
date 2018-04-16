from __future__ import unicode_literals

from django.db import models as dbmodels

from django.contrib.auth import models as usmodels
# Create your models here.

class Question(dbmodels.Model):
 title = dbmodels.CharField(max_length = 255)
 text = dbmodels.TextField()
 added_at = dbmodels.DateTimeField()
 rating = dbmodels.IntegerField()
 author = dbmodels.ManyToManyField(usmodels.User)
 likes = dbmodels.ManyToManyField(usmodels.User,related_name="question_like_user")

class Answer(dbmodels.Model):
 text = dbmodels.TextField()
 added_at = dbmodels.DateTimeField()
 question = dbmodels.ForeignKey(Question)
 author = dbmodels.ManyToManyField(usmodels.User)

class QuestionManager(dbmodels.Manager):
 def new(self):
  last_q = Question.objects.order_by("added_at")
  return last_q
 def popular(self):
  return Question.objects.order_by("rating")
  
