from django.db import models

choices_list = [('New','new'), ('In progress', 'in progress'), ('Done', 'done')]

class Tasks(models.Model):
    descr = models.CharField(max_length=100, null=False, blank=False, verbose_name='Description')
    status = models.CharField(max_length=50, null=False, blank=False,
                              choices=choices_list, default=choices_list[0][0], verbose_name='Status')
    completion_date = models.DateField(auto_now=False, null=True, blank=True, verbose_name='Completion date')
    full_description= models.TextField(max_length='3000', null=True, blank=True, verbose_name='Full description')

    def __str__(self):
        return  self.descr