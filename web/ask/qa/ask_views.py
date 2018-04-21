from django.shortcuts import render
from qa.forms import AskForm
from django.core.urlresolvers import reverse

def q_add(request):
 if request.method == "GET":
  return render(request,'q_add.html',{
   'form': AskForm(),
})
 else:
  form = AskForm(request.POST)
  if form.is_valid():
   q = form.save()
   return HttpResponseRedirect(reverse('ask'))
