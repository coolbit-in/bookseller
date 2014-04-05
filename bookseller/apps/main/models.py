from django.db import models
from django.contrib.auth.models import User

class Tags(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s' % self.id

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField()
    queue = models.ManyToManyField(User)
    tag = models.ManyToManyField(Tags)
    status = models.IntegerField()
    published_time = models.DateTimeField(auto_now=True)
    picture_url = models.URLField()

    def __unicode__(self):
        return u'%s %s' % (self.id, self.title)

class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.ForeignKey(Item, related_name='images')
    image = models.ImageField(upload_to='image_%Y_%m_%d')

class Messages(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    item_id = models.ForeignKey(Item)
    from_id = models.ForeignKey(User, related_name='from')
    to_id = models.ForeignKey(User, related_name='towards')
    published_time = models.TimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.published_time)


