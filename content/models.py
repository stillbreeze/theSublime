from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class PostManager(object):
	pass
		
class Post(models.Model):
	postTitle = models.CharField(_("Post title"),max_length=255)
	objects = PostManager()

	def __str__(self):
		return self.postTitle


class CommentManager(object):
	pass
		
class Comment(models.Model):
	objects = PostManager()

	def __str__(self):
		return self.pk


class SubCommentManager(object):
	pass

class SubComment(models.Model):
	objects = SubCommentManager()

	def __str__(self):
		return self.pk