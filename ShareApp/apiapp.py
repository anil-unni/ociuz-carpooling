from django.shortcuts import get_object_or_404
from rest_framework .response import Response
from rest_framework .views import APIView
from rest_framework import status
from .serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
import datetime
#function for user registration
class user_reg(APIView):
	data={}	
	def post(self,request):
		if request.method=="POST":
			User_Name=request.POST.get("User_Name")
			User_Password=request.POST.get("User_Password")
			User_Email=request.POST.get("User_Email")
			User_Phone=request.POST.get("User_Phone")

			if Tbl_User.objects.filter(User_Email=User_Email).exists():
				data={'status':'false','message':'E-mail already exists'}
				return Response(data)
			else:
				serializer=Tbl_User(User_Status="True",User_Name=User_Name,User_Password=User_Password,User_Email=User_Email,User_Phone=User_Phone,User_Type="User")
				serializer.save()
				data={'status':'true','message':'Thankyou for registration '}
				return Response(data)


#function for user login
class user_login(APIView):
	data={}
	def post(self,request):
		if request.method=="POST":
			User_Email=request.POST.get("User_Email")
			print(User_Email)
			User_Password=request.POST.get("User_Password")
			print(User_Password)
			chk=Tbl_User.objects.filter(User_Email=User_Email,User_Password=User_Password)
			print(chk)
			for x in chk:
				idd=x.id
			res=Tbl_User.objects.filter(id=idd,User_Email=User_Email,User_Password=User_Password)
			serializer_user = user_tbSerializer(res,many=True)
			data={'data':serializer_user.data}
			return Response(data)			


#function for adding route
class add_route(APIView):
	data={}	
	def post(self,request):
		if request.method=="POST":
			Start_Point=request.POST.get("Start_Point")
			End_Point=request.POST.get("End_Point")
			Date=request.POST.get("Date")
			Time=request.POST.get("Time")
			Vehicle_Type=request.POST.get("Vehicle_Type")
			User_ID=request.POST.get("User_ID")
			user_id=int(User_ID)
			uid=Tbl_User.objects.all().get(id=user_id)
			res=Tbl_Route.objects.filter(User_ID=uid,Start_Point=Start_Point,End_Point=End_Point,Date=Date,Time=Time,Vehicle_Type=Vehicle_Type)
			serializer_route = route_tbSerializer(res,many=True)
			data={'data':serializer_route.data}
			return Response(data)			

