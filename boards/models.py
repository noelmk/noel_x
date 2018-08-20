from django.db import models
from django.conf import settings

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.auth import get_user_model
# Create your models here.

class CommonFields(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT )
	# TODO: Properly format related names
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = '%(app_label)s_%(class)s_created_by_set', on_delete=models.PROTECT )
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = '%(app_label)s_%(class)s_updated_by_set', on_delete=models.PROTECT)
	class Meta:
		abstract = True

class LogicBlock(models.Model):
	block_type = models.CharField(max_length=10)
	# params = models.ManyTo

class TriggerAction(CommonFields):
	'''Triggers can belong to categories or anything else'''
	name = models.CharField(max_length=200)
	trigger = models.ForeignKey('Trigger', on_delete=models.PROTECT)

class Trigger(CommonFields):
	'''Triggers can belong to categories or anything else'''
	name = models.CharField(max_length=200)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	# a trigger has actions
	# a trigger could track its excution
	is_tiggered = models.BooleanField(default=False)


class Rating(CommonFields):
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	rating = models.PositiveIntegerField()
	justification = models.TextField()
	caveat = models.TextField(blank=True)

class Risk(CommonFields):
	name = models.CharField(max_length=200)

class Category(CommonFields):
	name = models.CharField(max_length=200)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	class Meta:
		verbose_name_plural = 'Categories'

class Attribute(CommonFields):
	name = models.CharField(max_length=200)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

class Evidence(CommonFields):
	source = models.CharField(max_length=50, choices=[('A','A'), ('B', 'B')])
	evidence_type = models.CharField(max_length=50, choices=[('A','A'), ('B', 'B')])
	age  = models.PositiveIntegerField()

class WeightConfig(CommonFields):
	board = models.ForeignKey('Board', on_delete=models.PROTECT)
	source = models.PositiveIntegerField()
	evidence_type = models.PositiveIntegerField()
	age = models.PositiveIntegerField()

# class Suggestion(models.Model):
#	# Suggestions can be provided for a board based on its config
# 	pass

class Board(CommonFields):
	# geographic focus
	geographic_focus = models.CharField(max_length=200)

	# and other 
	# Board has roles and users/admins
	# Weight configs

