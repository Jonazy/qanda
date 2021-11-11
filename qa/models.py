from django.db import models
from users.models import CustomUser
from django.shortcuts import reverse
# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(to=CustomUser, related_name='questions', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('qa:question', kwargs={'pk': self.id})

    def can_accept_answers(self, user):
        return user == self.user


class Answer(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(to=Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.TextField()
    accept = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer

    class Meta:
        ordering = ('-created_at',)
