from django.shortcuts import render
from .models import Question,Choice
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import urllib,base64
import matplotlib.pyplot as plt
import io
# Create your views here.

def index(request):
    data=Question.objects.order_by('pub_date')[:5]
    all_data={'latest_detail':data}
    return render(request,'polls/index.html',all_data)

def details(request,questions_id):
    try:
        question=Question.objects.get(pk=questions_id)
    except Question.DoesNotExist:
        raise Http404("Quesion does not existe")
    return render(request,'polls/detail.html',{'question':question})

# def vote(request,questions_id):

#     question=get_object_or_404(Question,pk=questions_id)
#     try:
#         selected_choice=question.choice_set.get(pk=request.POST['choice'])
#     except(KeyError,Choice.DoesNotExist):

#         return render(request,'polls/detail.html',{'question:':question,'error_message':"you don't select a choice",})
    
#     else:
#         selected_choice.vote += 1
#         selected_choice.save()

#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def vote(request, question_id):  # Ensure 'question_id' is here
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        print(selected_choice.vote)
        print("complete the selected choice")
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))

def result(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    labels=[]
    choices=question.choice_set.all()
    labels=[choice.choice_text for choice in choices]
    data=[choice.vote for choice in choices]
    # labels = ["apple", "orange", "banana", "mango", "grape"]

     # Create the plot
    plt.figure(figsize=(10, 5))
    plt.bar(labels, data, color='lightblue')
    plt.title(f'Votes for {question.question_text}')
    plt.xlabel('Choices')
    plt.ylabel('Votes')

    # Save it to a string buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image as a base64 string
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    return render(request, 'polls/result.html', { "labels": labels,
        "data": data,'question':question,'chart':graph})                        
