from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from qa.forms import QuestionForm
from qa.models import Question, Answer
from django.http import HttpResponseBadRequest

# Create your views here.


class QuestionView(LoginRequiredMixin, CreateView):
    form_class = QuestionForm
    template_name = 'qa/questions.html'

    def get_initial(self):
        return {
            "user": self.request.user.id
        }

    def form_valid(self, form):
        action = self.request.method.POST.get('action',)
        if action == 'SAVE':
            return super.form_valid(form)
        elif action == 'PREVIEW':
            preview = Question(
                question=form.cleaned_data['question'],
                title=form.cleaned_data['title'],
            )
            context = self.get_context_data(preview=preview)
            return self.render_to_response(context=context)
        return HttpResponseBadRequest()