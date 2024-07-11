from django.db import models
from django.utils import timezone

# Create your models here.
class scriptingLang(models.Model):
    LANG_TYPE_CHOICE = [
        ('Js', 'JavaScript'),
        ('JSX', 'Javascript_Extension'),
        ('Rb', 'Ruby'),
        ('JAVA', 'Java'),
        ('Py', 'Python'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='firstapp/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=4, choices=LANG_TYPE_CHOICE)
    description = models.TextField(default='')
    def __str__(self):
        return self.name