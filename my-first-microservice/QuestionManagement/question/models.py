from django.db import models

# Create your models here.

class Question(models.Model):
    owner_id = models.PositiveIntegerField()
    title = models.CharField(max_length=80)
    body = models.TextField(max_length=800)
    is_removed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner_id} - {self.title}'