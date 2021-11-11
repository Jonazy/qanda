from django import forms
from qa.models import Question, Answer
from users.models import CustomUser


class QuestionForm(forms.ModelForm):
    user = forms.ModelChoiceField(widget=forms.HiddenInput,
                                  queryset=CustomUser.objects.all(), disabled=True, )

    class Meta:
        model = Question
        fields = ['title', 'question', 'user']


class AnswerForm(forms.ModelForm):
    user = forms.ModelChoiceField(widget=forms.HiddenInput,
                                  queryset=CustomUser.objects.all(), disabled=True, )
    question = forms.ModelChoiceField(widget=forms.HiddenInput,
                                      queryset=Question.objects.all(), disabled=True, )

    class Meta:
        model = Answer
        fields = ['answer', 'question', 'user']


class AnswerAcceptanceForm(forms.ModelForm):
    accepted = forms.BooleanField(widget=forms.HiddenInput, required=False,)

    class Meta:
        model = Answer
        fields = ['accepted',]
