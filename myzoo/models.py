# -*- coding: utf-8 -*-
import time
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30,blank=True, null=True)
    password = models.CharField(max_length=30,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now = True)
    avatar = models.ImageField('头像',upload_to='avatar/%Y/%m/%d',default='',
                               blank=True, null=True)
    
    def isvalidity(self):
        if self.password<6:
            return False
        else:
            return True

    def __unicode__(self):
        return self.username


class Pet(models.Model):
	TYPE_CHOICES=(('cat','cat'),
	              ('dog','dog'),
	              ('other','other'),
	)
	name = models.CharField(max_length=30,blank=True, null=True)
	avatar_uri = models.URLField(blank=True, null=True)
	user = models.ForeignKey(User) 
	created_date = models.DateTimeField(auto_now = True)
	type = models.CharField(max_length=30, choices=TYPE_CHOICES)
	def __unicode__(self):
		return self.name

class Photo(models.Model):
    image_uri=models.URLField(blank=True, null=True)
    pet = models.ForeignKey(Pet)
    user = models.ForeignKey(User)
    text = models.TextField(blank=True, null=True,
                            verbose_name="Description")
    like_count = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now = True)
    class Meta:
        ordering= ['-created_date',]

	
	
	
	
