from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404 
from django.http import HttpResponse , HttpResponseRedirect , JsonResponse , Http404
from django.urls import reverse

from .models import Question , Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request , 'polls/index.html' , context)

def detail(request , pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request , 'polls/results.html', {'question':question})

def results(request , pk):
    question = get_object_or_404(Question , pk=pk)
    return render(request , 'polls/results.html' , {'question':question})

def vote(request , pk):
    question = get_object_or_404(Question , pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError , Choice.DoesNotExist):
        return render(request , 'polls/detail.html' , {
            'question':question,
            'error_message':'you did not select a choice',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results' , args=(question.id,)))
    
    
def resultsData(request , obj):
    votedata = []
    question = Question.objects.get(id=obj)
    votes = question.choice_set.all()
    
    for i  in votes:
        votedata.append({i.choice_text:i.votes})
        
    print(votedata)
    return JsonResponse(votedata , safe=False)