from __future__ import unicode_literals

from django.db import models as dbmodels

from django.contrib.auth import models as usmodels
# Create your models here.

class QuestionManager(dbmodels.Manager):
 def new(self):
  return self.order_by("added_at")
 def popular(self):
  return self.order_by("rating")

class Question(dbmodels.Model):
 title = dbmodels.CharField(max_length = 255)
 text = dbmodels.TextField()
 added_at = dbmodels.DateTimeField(blank=True,auto_now_add=True)
 rating = dbmodels.IntegerField(default=10)
 author = dbmodels.ForeignKey(usmodels.User)
 likes = dbmodels.ManyToManyField(usmodels.User,related_name="question_like_user")
 objects = QuestionManager()


class Answer(dbmodels.Model):
 text = dbmodels.TextField()
 added_at = dbmodels.DateTimeField()
 question = dbmodels.ForeignKey(Question)
 author = dbmodels.ForeignKey(usmodels.User)


