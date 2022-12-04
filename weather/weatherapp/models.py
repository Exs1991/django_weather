from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты'
