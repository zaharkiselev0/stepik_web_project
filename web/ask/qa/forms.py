from django import forms
from qa.models import Question

class AskForm(forms.Form):
 title = forms.CharField(max_length=100)
 text = forms.CharField(widget=forms.Textarea)
 def clean(self):
  return self.cleaned_data 
 def save(self):
  q = Question(**self.cleaned_data)
  q.save()
  return q

class AnswerForm(forms.Form):
 text = forms.CharField(widget=forms.Textarea)
 question = forms.IntegerField()
 def clean(self):
  return self.cleaned_data
 def save(self):
  q = Question.objects.get(id = question)
  a = Answer(text=self.text,question=q)
  a.save()
  return a

