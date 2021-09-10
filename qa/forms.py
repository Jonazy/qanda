from django import forms
from qa.models import Question, Answer
from users.models import CustomUser


class QuestionForm(forms.ModelForm):
    user = forms.ModelChoiceField(widget=forms.HiddenInput,
                                  queryset=CustomUser.objects.all, disabled=True,)

    class Meta:
        model = Question
        fields = ['title', 'question', 'user']
