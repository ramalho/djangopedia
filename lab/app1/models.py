from django.db import models

class EmptyModel(models.Model):
    pass

class OneFieldModel(models.Model):
    title = models.CharField(max_length=64, blank=True)
    
    def __unicode__(self):
        return '#%s: %s' % (self.id, self.title)

