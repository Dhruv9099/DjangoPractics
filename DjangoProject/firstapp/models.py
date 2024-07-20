from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
    
# One to Many relationship:
# review is associated with scripting language
class ScriptLangReview(models.Model):
    script = models.ForeignKey(scriptingLang, on_delete=models.CASCADE,related_name ='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment =models.TextField()
    date_added =models.DateTimeField(default = timezone.now)    
    
    def __str__(self):
        return f'{self.user.username} review for {self.script.name}'


# many to many

class ScriptsStore(models.Model):
    name = models.CharField( max_length=50)
    location= models.CharField( max_length=50)
    script_varieties = models.ManyToManyField(scriptingLang, related_name='ScriptsStore')
    
    def __str__(self):
        return  self.name

# one to one
class scriptCertificates(models.Model):
    script = models.OneToOneField(scriptingLang, related_name='certificate', on_delete=models.CASCADE)
    certificate_number = models.CharField(max_length=50)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until= models.DateTimeField()
    
    
    def __str__(self):
        return f'Certificate for {self.script.name}'
    
    # do migration
    # python  manage.py makemigrations
    # python manage.py migrate
    # python mange.py runserver 
    # goto admin.py
    # import above class from .models
    # class chai