from django.db import models
class Notes(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    content=models.TextField()
    def __unicode__(self):
	return self.title
#class Notes(models.Model):
   # author=models.CharField(max_length=255)
   # content=models.TextField()
   #def __unicode__(self):
       # return self.author

# Create your models here.
