# from django import forms
# from django.shortcuts import redirect
#
# from .models import Test, Question
#
#
# class TestForm(forms.ModelForm):
#     class Meta:
#         model = Test
#         fields = ('title', 'category', 'maximum_attemps', 'start_date', 'and_date', 'pass_percentage')
#
#     def save(self, commit=True):
#         test = self.instance
#         test.author = request.user
#         super().save(commit)
#         return test.id
#
# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ('question', 'a', 'b', 'c', 'd', 'true_answer')
#     submit_and_exit = forms.BooleanField(required=False)
#
#     def save(self, commit=True):
#         question = self.instance
#         question.test = Test.objects.filter(id=test_id)
#         super().save(commit)
#         return question


from django import forms
from .models import Test, Question


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = (
            'title',
            'category',
            'maximum_attemps',
            'start_date',
            'end_date',  # oldingi xatolik: 'and_date' bo'lishi kerak emas
            'pass_percentage',
        )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # request ni tashqaridan olish
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        test = super().save(commit=False)
        if self.request:
            test.author = self.request.user  # test yaratuvchisini belgilash
        if commit:
            test.save()
        return test.id


class QuestionForm(forms.ModelForm):
    submit_and_exit = forms.BooleanField(required=False)  # bu qo‘shimcha checkbox

    class Meta:
        model = Question
        fields = (
            'question',
            'a',
            'b',
            'c',
            'd',
            'true_answer',
        )

    def __init__(self, *args, **kwargs):
        self.test = kwargs.pop('test', None)  # test obyektini tashqaridan olish
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        question = super().save(commit=False)
        if self.test:
            question.test = self.test  # bog‘liq testni belgilash
        if commit:
            question.save()
        return question
