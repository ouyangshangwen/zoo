#!/usr/bin/python   
# -*- coding: utf-8 -*-

import sys,os
import time
import md5
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Template,Context
from django.shortcuts import render_to_response
from django.template import loader,Context
from django.utils import simplejson
from django.core import serializers

from zoo.myzoo.models import User,Pet,Photo

def md5_encode(str):

    return md5.new(str).hexdigest()

def login(request):
	if request.method=='POST':
		try:
			user=User.objects.get(email=request.POST['email'])
			request.session['email']=user.email
		except User.DoesNotExist:
			return render_to_response('login.html')

		return HttpResponseRedirect('/gravatar/')

	return render_to_response('login.html')	
def gravatar(request):
	
	email=request.session['email']
	return render_to_response('gravatar.html', {'avatar': email})
	

def resgister(request):
	if request.method=='POST':
		email=request.POST['email']
		username=request.POST['username']
		password=md5_encode(request.POST['password'])
		user=User(username=username,email=email,password=password)
		user.save()
		return HttpResponseRedirect('/login/')

	return render_to_response('signup.html')
 
from pymongo import Connection,DESCENDING
import random
from datetime import *  
from pymongo import Connection
from datetime import *    
def printx(request):
#    createdata()
    db=conndb()

    totals=db.Photo.count()
    latestnum=int(totals*0.2)
    start=datetime.utcnow()-timedelta(days=5)
    end=datetime.utcnow()-timedelta(days=90)
    catphotos=db.Photo.find({"created_data":{"$lte":start,"$gte":end},"pet.type":"cat"}).limit(latestnum*2)
    latestphotos= db.Photo.find({"created_data":{"$gte":start}}).sort("like_count",DESCENDING).limit(latestnum)
    
    otherphotos=db.Photo.find({"created_data":{"$lte":start,"$gte":end},"pet.type":{"$ne":"cat"}}).limit(latestnum*2)
    return render_to_response('selfpage.html',{'latestphotos':latestphotos,'catphotos':catphotos,'otherphotos':otherphotos})
  
def conndb():

    conn=Connection()
    db=conn.mydb
    return db

def createdata():

    db=conndb()
    for photonum in range(1000):
        pet_list=['cat','dog','other']
        month=random.randint(1,6)
        days=random.randint(0,150)
        created_data=datetime.utcnow()-timedelta(days=days)
        petype=random.choice(pet_list)
        like_count=random.randint(0,100)
        db.Photo.save({'pet':{'name':photonum,'type':petype},'like_count':like_count,'created_data':created_data})

    














