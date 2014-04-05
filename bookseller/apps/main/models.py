from django.db import models
from django.contrib.auth.models import User

<<<<<<< Updated upstream

class Books(models.Model):
    id = models.IntegerField(primary_key=True)
=======
class Tags(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s' % self.name

class Item(models.Model):
>>>>>>> Stashed changes
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField()
    queue = models.ManyToManyField(User)
    number = models.IntegerField()
    tag = models.ManyToManyField(Tags)
    status = models.IntegerField()
<<<<<<< Updated upstream
    published_time = models.TimeField(auto_now=True)
    picture_url = models.URLField()
=======
    published_time = models.DateTimeField(auto_now=True)
>>>>>>> Stashed changes

    def __unicode__(self):
        return u'%s %s' % (self.id, self.title)

<<<<<<< Updated upstream
class Tags(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s' % self.id
=======
class Image(models.Model):
    item_id = models.ForeignKey(Item, related_name='images')
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='image_%Y_%m_%d')
>>>>>>> Stashed changes


    def __unicode__(self):
        return 'Image' + str(self.name)

class Messages(models.Model):
    content = models.TextField()
<<<<<<< Updated upstream
    Book_id = models.ForeignKey(Books)
    from_id = models.ForeignKey(User)
    to_id = models.ForeignKey(User)
    published_time = models.TimeField(auto_now=True)
=======
    item_id = models.ForeignKey(Item)
    from_id = models.ForeignKey(User, related_name='from')
    to_id = models.ForeignKey(User, related_name='towards')
    published_time = models.DateTimeField(auto_now=True)
>>>>>>> Stashed changes

    def __unicode__(self):
        return u'%s %s' % (self.id, self.published_time)


