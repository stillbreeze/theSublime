from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class TopicManager(object):
	pass
		

class Topic(models.Model):
	topicName = models.CharField(_("Topic name"),max_length=255)
	objects = TopicManager()

	def __str__(self):
		return self.topicName

class SubTopicManager(object):
	pass
		

class SubTopic(models.Model):
	subTopicName = models.CharField(_("Sub-topic name"),max_length=255)
	objects = SubTopicManager()
	def __str__(self):
		return self.subTopicName
		