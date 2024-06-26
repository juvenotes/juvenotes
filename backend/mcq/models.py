import datetime

from django.db import models

from common.models import IndexedTimeStampedModel

# from library.models import Unit
from users.models import User


# unit model
class Unit(IndexedTimeStampedModel):
    owner = models.ForeignKey(User,
                              related_name='units_created',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    class Meta:
        unique_together = ('title', 'id')

    def __str__(self):
        return self.title

# quiz model
class Quiz(IndexedTimeStampedModel):
    # def year_choices(model_name):
    #     current_year = datetime.datetime.now().year
    #     return [(f"{year}_{model_name}", year) for year in range(2000, current_year + 1)]

    # YEARS_CHOICES = year_choices('Quiz')

    owner = models.ForeignKey(User,
                              related_name='quizzes_created',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    # New fields, for year and tags when we bundle quizzes and create a unified qbank for a unit if someone wants it
    year = models.IntegerField(('year'), blank=False, default=2024)
    paper_type = models.CharField(max_length=255, choices=[('EOR', 'End of Rotation'), ('EOY', 'End of Year')], blank=False, default='EOR')
    related_topic = models.ForeignKey(Unit, related_name='related_questions', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('title', 'id')
        verbose_name_plural = "quizzes"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.related_topic is None:
            self.related_topic = self.unit
        super().save(*args, **kwargs)


# question model
class Question(IndexedTimeStampedModel):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    related_topic = models.ForeignKey(Unit, related_name='related_quizzes', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('text', 'id')

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        if self.related_topic is None:
            self.related_topic = self.quiz.unit
        super().save(*args, **kwargs)

# choices model
class Choice(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)


    def __str__(self):
        return f"Choice(text={self.text}, is_correct={self.is_correct})"


# feedback model
class Feedback(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, related_name='feedback', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
