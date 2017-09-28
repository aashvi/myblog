# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from blog.models import Post

# Create your views here.

def detail(request):
	
	post= Post.objects.all()
	context = {
	  'post' : post
	}

	return render(request, 'home.html', context)



def post(request, post_id):
	print post_id
	post= Post.objects.get(pk=post_id)
	print post.title

	context = {
	  'post' : post
	}

	return render(request, 'post.html', context)