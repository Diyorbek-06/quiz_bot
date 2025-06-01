from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Test, Question
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    test = Test.objects.all()
    return render(request, 'index.html', {'test':test})

@login_required(login_url='login')
def ready_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    return render(request, 'ready_test', {'test':test})

@login_required(login_url='login')
def test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    question = Question.objects.filter(test=test)

    contex = {'test': test, 'question':question}
    return render(request, 'test.html', contex)