from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from qa.forms import QuestionForm, AnswerForm, AnswerAcceptanceForm
from qa.models import Question, Answer
from django.http import HttpResponseBadRequest

# Create your views here.


class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'qa/questions.html'


class QuestionView(CreateView):
    form_class = QuestionForm
    template_name = 'qa/add_question.html'

    def get_initial(self):
        return {
            "user": self.request.user.id
        }

    # def form_valid(self, form):
    #     action = self.request.method.POST.get('action',)
    #     if action == 'SAVE':
    #         return super.form_valid(form)
    #     elif action == 'PREVIEW':
    #         preview = Question(
    #             question=form.cleaned_data['question'],
    #             title=form.cleaned_data['title'],
    #         )
    #         context = self.get_context_data(preview=preview)
    #         return self.render_to_response(context=context)
    #     return HttpResponseBadRequest()


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'qa/question_details.html'
    context_object_name = 'question_detail'

    ACCEPT_FORM = AnswerAcceptanceForm(initial={'accepted': True})
    REJECTED_FORM = AnswerAcceptanceForm(initial={'accepted': False})

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data()
        context.update({
            'answer_form': AnswerAcceptanceForm(initial={
                'user': self.request.user,
                'question': self.object.id,
            })
        })
        if self.object.can_accept_answers:
            context.update({
                'accept_form': self.ACCEPT_FORM,
                'reject_form': self.REJECTED_FORM,
            })
        return context


class CreateAnswerView(CreateView):
    form_class = AnswerForm
    template_name = 'qa/add_answer.html'

    def get_initial(self):
        return {
            'user': self.request.user.id,
            'question': self.get_question().id,
        }

    def get_context_data(self, **kwargs):
        return super().get_context_data(question=self.get_question(), **kwargs)

    def get_success_url(self):
        return self.object.question.get_absolute_url()

    def get_question(self):
        return Question.objects.get(pk=self.kwargs['pk'])
