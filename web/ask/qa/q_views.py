from django.shortcuts import render, get_object_or_404
from qa.models import Answer, Question, QuestionManager
from django.core.paginator import Paginator

def main(request,sorted = "new"):
 if sorted == "popular":
  questions = Question.objects.popular()
 else:
  questions = Question.objects.new()
 page = request.GET.get("page",1)
 limit = 10
 paginator = Paginator(questions,limit)
 paginator.baseurl = '/?page='
 page = paginator.page(page)
 return render(request, 'main.html', {
  'questions': page.object_list,
  'paginator': paginator,
  'page': page,
})

def popular(request):
 return main(request,"popular")

def question(request,id):
 q = get_object_or_404(Question, id=id)
 answers = Answer.objects.filter(question=q)
 return render(request, 'question.html', {
  'q': q,
  'answers': answers,
})
