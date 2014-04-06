from django.db import models
from django.contrib.auth.models import User


class Tags(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __unicode__(self):
        return u'%s' % self.name


class Item(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField()
    queue = models.ManyToManyField(User)
    number = models.IntegerField()
    left_number = models.IntegerField()
    tag = models.ForeignKey(Tags)
    status = models.IntegerField()
    published_time = models.DateTimeField(auto_now=True)
    lasted_update_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image_%Y_%m_%d')

    def if_available(self):
        if self.left_number > 0:
            return True
        else:
            return False

    def if_has_image(self):
        if self.image == '':
            return False
        else:
            return True

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

class UserInfo(models.Model):
    user_id = models.ForeignKey(User)
    phone_number = models.IntegerField(max_length=11)
    qq_number = models.IntegerField(max_length=15)
    address = models.TextField(max_length=256)

