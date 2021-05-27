from django.db import models
from django.conf import settings
from django.urls.base import reverse


class Question(models.Model):
    title = models.CharField(max_length=140, verbose_name='Название')
    question = models.TextField(verbose_name='Вопрос')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('qanda:question_detail', kwargs={'pk': self.id})

    def can_accept_answers(self, user):
        return user == self.user

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    answer = models.TextField(verbose_name='Ответ')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

