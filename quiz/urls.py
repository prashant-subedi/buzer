from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^home$',views.press,name="pressed"),
	url(r'^particpantBuzzer$',views.pressed,name="presseded"),
	url(r'^nowpress$',views.quizAdmin,name="nowressed")

]