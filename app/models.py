from django.db import models

# Create your models here.
class Note(models.Model):
    user=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.user
    
class Notestore(models.Model):
    Note_user=models.ForeignKey(Note,on_delete=models.CASCADE)
    Note_id=models.IntegerField(primary_key=True)
    title=models.TextField(max_length=50)
    content=models.CharField(max_length=100)
    text=models.TextField(max_length=100)
    
    AUDIO='audio'
    VIDEO='video'
    TYPE_CHOICES=[
        (AUDIO,'Audio'),
        (VIDEO,'video'),
    ]
    type=models.CharField(max_length=100,choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.title
