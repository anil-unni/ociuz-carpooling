from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Tbl_User(models.Model):
	User_Name    				=models.CharField(max_length=300,default='')
	User_Password				=models.CharField(max_length=50,default='')
	User_Email					=models.CharField(max_length=300,default='')
	User_Phone					=models.CharField(max_length=200,default='')
	User_Type					=models.CharField(max_length=200,default='')
	User_Status					=models.CharField(max_length=200,default='')


class Tbl_Route(models.Model):
	User_ID             =models.ForeignKey(Tbl_User,on_delete=models.CASCADE, blank=True,null=True)
	Start_Point    		=models.CharField(max_length=300,default='')
	End_Point			=models.CharField(max_length=500,default='')
	Date				=models.CharField(max_length=300,default='')
	Time				=models.CharField(max_length=200,default='')
	Vehicle_Type		=models.CharField(max_length=200,default='')

class user_registration_tb(models.Model):
	name               =models.CharField(max_length=300,default='')
	emailid            =models.CharField(max_length=300,default='')
	gender             =models.CharField(max_length=300,default='')
	password           =models.CharField(max_length=300,default='')
	mobile_Number      =models.CharField(max_length=300,default='')
	id_proof           =models.CharField(max_length=300,default='')
	id_number          =models.CharField(max_length=300,default='')
	user_type          =models.CharField(max_length=300,default='0')
	location           =models.CharField(max_length=300,default='0')

class VehicleSharing(models.Model):
    start           =models.CharField(max_length=300,default='')
    dest            =models.CharField(max_length=300,default='')
    cost            =models.IntegerField(default='')
    date            =models.DateField(max_length=300,default='')
    start_time      =models.CharField(max_length=300,default='')
    arrival_time    =models.CharField(max_length=300,default='')
    no_pass         =models.IntegerField(default='')
    details         =models.TextField(max_length=300,default='')
    gender          =models.CharField(max_length=300,default='')
    status1         =models.CharField(max_length=300,default='')
    status2         =models.CharField(max_length=300,default='')
    user            =models.ForeignKey(user_registration_tb, on_delete=models.CASCADE)
 
class Tbl_Request(models.Model):
    start           =models.CharField(max_length=300,default='')
    dest            =models.CharField(max_length=300,default='')
    cost            =models.IntegerField(default='')
    arrival_time    =models.CharField(max_length=300,default='')
    status          =models.CharField(max_length=300,default='')
    u_id            =models.ForeignKey(user_registration_tb, on_delete=models.CASCADE,default='')
    v_id            =models.ForeignKey(VehicleSharing, on_delete=models.CASCADE,default='')
    driver_id       =models.CharField(max_length=300,default='')
    link            =models.CharField(max_length=300,default='')
    time            =models.CharField(max_length=300,default='')
    date            =models.CharField(max_length=300,default='')
    cur_date        =models.CharField(max_length=300,default='')





class Tbl_feedback(models.Model):
    user            =models.ForeignKey(user_registration_tb, on_delete=models.CASCADE)
    star_rating     =models.CharField(max_length=300,default='')
    suggestion      =models.CharField(max_length=300,default='')
    ext1            =models.CharField(max_length=300,default='')
    ext2            =models.CharField(max_length=300,default='')


	