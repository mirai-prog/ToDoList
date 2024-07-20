from django.db import models

# Create your models here.


class ToDo(models.Model):
    title = models.CharField('Note name', max_length=500)
    is_complete = models.BooleanField('Complete', default=False)
    
    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
    
    def __str__(self):
        return self.title