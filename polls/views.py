from django.shortcuts import render
from .models import Question,Choice
from django.shortcuts import get_object_or_404
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








