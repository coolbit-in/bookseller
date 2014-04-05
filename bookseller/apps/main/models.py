from django.db import models
from django.contrib.auth.models import User


class Tags(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s' % self.name

class Item(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField()
    queue = models.ManyToManyField(User)
    number = models.IntegerField()
    tag = models.ManyToManyField(Tags)
    status = models.IntegerField()
    published_time = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return u'%s %s' % (self.id, self.title)


class Image(models.Model):
    item_id = models.ForeignKey(Item, related_name='images')
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='image_%Y_%m_%d')



    def __unicode__(self):
        return 'Image' + str(self.name)

class Messages(models.Model):
    content = models.TextField()
    item_id = models.ForeignKey(Item)
    from_id = models.ForeignKey(User, related_name='from')
    to_id = models.ForeignKey(User, related_name='towards')
    published_time = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return u'%s %s' % (self.id, self.published_time)


