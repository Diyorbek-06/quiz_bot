from django.db.transaction import savepoint
from django.shortcuts import render, get_object_or_404, redirect
from .models import Test, Question, CheckTest, CheckQuestion
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from.forms import TestForm, QuestionForm
# Create your views here.

def index(request):
    test = Test.objects.all()
    return render(request, 'index.html', {'test':test})

@login_required(login_url='login')
def ready_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    return render(request, 'ready_test.html', {'test':test})

@login_required(login_url='login')
def test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    attemps = CheckTest.objects.filter(student=request.user, test=test).count()
    if (timezone.now() > test.start_date and timezone.now() < test.end_date) and attemps < test.max_attemps:
        questions = Question.objects.filter(test=test)
        if request.method == 'POST':
            checktest = CheckTest.objects.create(student=request.user, test=test)
            for question in questions:
                given_answer = request.POST.get(str(question.id), '')
                CheckQuestion.objects.create(checktest=checktest, question=question, given_answer=given_answer)

                # given_answer = request.POST[str(question.id)]
                # CheckQuestion.objects.create(checktest=checktest, question=question, given_answer=given_answer.true_answer)
            checktest.save()
            return redirect("checktest" , checktest.id)
        context = {'test': test, 'questions':questions}
        return render(request, 'test.html', context)
    else:
        return HttpResponse("Test not found!")

@login_required(login_url='login')
def checktest(request, checktest_id):
    checktest = get_object_or_404(CheckTest, id=checktest_id, student=request.user)
    return render(request, 'checktest.html', {'checktest':checktest})


@login_required(login_url='login')
def new_test(request):
    form = TestForm()
    if request.method=='POST':
        form = TestForm(data=request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.author = request.user
            test.save()
            return redirect('new_question', test.id)
            # test_id = form.save(request)
            # return redirect('new_question', test_id)
        return render(request, 'new_test.html', {'form':form})
    else:
        form = TestForm()
    return render(request, 'new_test.html', {'form': form})


@login_required(login_url='login')
def new_question(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if test.author == request.user:
        form = QuestionForm()
        test = get_object_or_404(Test, id=test_id)
        if request.method=='POST':
            form = QuestionForm(data=request.POST)
            if form.is_valid():
                form.save(test_id)
                if form.cleaned_data['submit_end_exit']:
                    return redirect('polite', request.user.id)
                return redirect("new_question", test.id)
            return render(request, 'new_question.html', {'form':form, 'test':test})
        else:
            return HttpResponse("Nimadir xatolik ketdi!")


