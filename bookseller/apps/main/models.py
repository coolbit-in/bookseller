from django.db import models
from django.contrib.auth.models import User

class Tags(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s' % self.id

class Books(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField()
    queue = models.ManyToManyField(User)
    tag = models.ManyToManyField(Tags)
    status = models.IntegerField()
    published_time = models.TimeField(auto_now=True)
    picture_url = models.URLField()

    def __unicode__(self):
        return u'%s %s' % (self.id, self.title)

class Messages(models.Model):
    content = models.TextField()
    Book_id = models.ForeignKey(Books)
    from_id = models.ForeignKey(User, related_name='from_id')
    to_id = models.ForeignKey(User, related_name='to_id')
    published_time = models.TimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.published_time)


