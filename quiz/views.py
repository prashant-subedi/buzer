from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import QuizModel
# Create your views here.

def press(request):
	if request.user.username=='quizadmin':
		return HttpResponse("""
			<html>
			<head></head>
			<body>
			<a href="nowpress">Free The Lock</a>
			""")
	else:
		return HttpResponse("""
			<html>
			<head></head>
			<body>
			<center>
			<a href="particpantBuzzer"><marquee><h1>Buzzer Button</a>
			</center>
			""")

def pressed(request): 
	lock=QuizModel.objects.all()[0]
	lock=lock.ready
	if lock==False:
		print(request.user)
		a=QuizModel.objects.all()[0]
		a.ready=True
		a.save()
		print(request.user.username)
		return HttpResponse("""Now Answer the Question
			<a href="home"><marquee><h1>Go back</a>"""
			)
	else:
		return HttpResponse("""Locked!!!
			<a href="home"><marquee><h1>Go Back</a>
			""")



def quizAdmin(request):
		print ("Lock set to true")
		a=QuizModel.objects.all()[0]
		a.ready=False
		a.save()
		return redirect('/quiz/home')
		