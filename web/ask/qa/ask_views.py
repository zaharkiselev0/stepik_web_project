from django.shortcuts import render
from qa.forms import AskForm

def q_add(request):
 if request.method == "GET":
  return render(request,'q_add.html',{
   'form': AskForm(),
})
 else:
  form = AskForm(request.POST)
  if form.is_valid():
   q = form.save()
   url = q.get_url()
   return HttpResponseRedirect(url)
