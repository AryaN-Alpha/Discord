from django.db import models
from django.contrib.auth.models import User

class Topic (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name[0:7]

# Create your models here.
class Room(models.Model):
    topic=models.ForeignKey(Topic , on_delete=models.SET_NULL , null=True)
    host= models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=  True , blank=True)
    participants= models.ManyToManyField(User , related_name='participants' , blank = True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created' , '-updated']

    def __str__(self):
        return self.name
    
class Message(models.Model):
    host= models.ForeignKey(User , on_delete=models.CASCADE)
    room = models.ForeignKey(Room , on_delete=models.CASCADE)
    body = models.TextField(blank=True , null=True )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-created']
    
    def __str__(self):
        return (self.body[0:50] if self.body else "None")  
    





