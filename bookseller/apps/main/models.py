from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    id = models.IntegerField(primary_key=True)
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

class Tags(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s' % self.id

class Messages(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    Book_id = models.ForeignKey(Books)
    from_id = models.ForeignKey(User)
    to_id = models.ForeignKey(User)
    published_time = models.TimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.published_time)


