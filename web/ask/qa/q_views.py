from django.shortcuts import render, get_object_or_404
from qa.models import Answer, Question, QuestionManager
from django.core.paginator import Paginator
from qa.forms import AnswerForm
from django.core.urlresolvers import reverse

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
 if request.method == "GET":
  q = get_object_or_404(Question,id=id)
  answers = Answer.objects.all()
  return render(request, 'question.html', {
   'q': q,
   'answers': answers,
   'form': AnswerForm(),
 })
 else:
  form = AnswerForm(request.POST)
  if form.is_valid():
   a = form.save()
   return HttpResponseRedirect(request.get_full_path())
