from django.shortcuts import render
from django.views.decorators.cache import cache_control
from .models import *
from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def index(request):
	return render(request,'index.html')
def admin_home(request):
    return render(request,'admin_home.html')
def feedback(request):
    var=Tbl_feedback.objects.all()
    return render(request,'view_feedback.html',{'var':var})

def rate_driver(request):
    if request.method == "POST":
        driver_id=request.POST["driverid"]
        journy_id=request.POST["travelid"]
        print("gggggggggggggggg  journy_id  gggggggggggggg",journy_id)

        commentText       = request.POST["commentText"]
        rating1        = request.POST["rating1"]
        pass_id=user_registration_tb.objects.all().get(id=driver_id)
        # jid=Tbl_Request.objects.all().get(id=journy_id)

        var=Tbl_feedback(user=pass_id,star_rating=rating1,suggestion=commentText)
        var.save()
        return HttpResponseRedirect('/view_status/')   
    else:
        ii=request.GET['id']
        var=Tbl_Request.objects.all().filter(id=ii)
        for x in var:
            dri_id=x.driver_id
        print("id of the rated driver is ", dri_id)
        return render(request,'service/add_rating.html',{'dri_id':dri_id,'ii':ii})


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def login(request):
    if request.method == "POST":
        email  		= request.POST["Username"]
        password 		= request.POST["password"]
        Superadmin 		= Tbl_User.objects.filter(User_Email=email, User_Password=password,User_Type="Admin")     
        if Superadmin:
            for x in Superadmin:
                request.session['id'] = x.id
            return render(request,'admin_home.html',{'success':'Succesfully LogedIn'})
      
        else:
        	return render(request, 'index.html')
    else:
    	return render(request, 'index.html')
    

def user_list(request):
    var=user_registration_tb.objects.all().filter(user_type="Driver")
    var1=user_registration_tb.objects.all().filter(user_type="Passenger")

    return render(request,'user_list.html',{'var':var,'var1':var1})
#user section
def list_ride(request):
    ii=request.session['id']
    # from datetime import date
    # # Returns the current local date
    # today = date.today()
    # print("Today date is: ", today)
    var=VehicleSharing.objects.all().filter(user=ii).order_by('date')
    
    
    return render(request, 'service/list_ride.html',{'var':var})
def all_ride(request):
    ii=request.session['id']
    var=VehicleSharing.objects.all().order_by('date')
    from django.db.models import Avg

    rr=Tbl_feedback.objects.all().aggregate(Avg('star_rating'))
    # print("ffffffffffffffffffffffff",rr.values())

    return render(request, 'service/list_all_ride.html',{'var':var})
def u_index(request):
    return render(request,'service/index.html')
def view_profile(request):
    ii=request.session['id']
    var=user_registration_tb.objects.all().filter(id=ii)
    for x in var:
        utype=x.user_type
    print("WWwwwwwwwwwwwwwwwwww   user type wwwwwwwwwwwwwwwww",utype)

    return render(request,'service/view_profile.html',{'db':var,'utype':utype})
def delete_ride(request):
    ii=request.GET['id']
    var=VehicleSharing.objects.all().filter(id=ii).delete()
    return HttpResponseRedirect('/list_ride/')
def remove_rideee(request):
    ii=request.GET['id']
    var=Tbl_Request.objects.all().filter(id=ii).delete()
    return HttpResponseRedirect('/view_status/')

def view_reqst(request):
    ii=request.session['id']
    import datetime
    xx=datetime.date.today() 
    print("cur dateeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",xx)
    
    var=Tbl_Request.objects.all().filter(driver_id=ii,status="requested")
    var1=Tbl_Request.objects.all().filter(driver_id=ii,status="Approved")
    var2=Tbl_Request.objects.all().filter(driver_id=ii,status="Rejected")
    var3=Tbl_Request.objects.all().filter(driver_id=ii,status="discussing")
    var4=Tbl_Request.objects.all().filter(driver_id=ii,status="Finished")




    return render(request,'service/list_request.html',{'var4':var4,'var':var,'var1':var1,'var2':var2,'var3':var3})
def reject_ride(request):
    ii=request.GET['id']
    var=Tbl_Request.objects.all().filter(id=ii).update(status="Rejected")
    return HttpResponseRedirect('/view_reqst/')


def reject_ride_pass(request):
    ii=request.GET['id']
    var=Tbl_Request.objects.all().filter(id=ii).update(status="Rejected")
    return HttpResponseRedirect('/view_status/')

def view_status(request):
    ii=request.session['id']
    var=Tbl_Request.objects.all().filter(u_id=ii,status="Approved")
    var1=Tbl_Request.objects.all().filter(u_id=ii,status="Finished")
    var3=Tbl_Request.objects.all().filter(u_id=ii,status="discussing")
    var4=Tbl_Request.objects.all().filter(u_id=ii,status="requested")
    var5=Tbl_Request.objects.all().filter(u_id=ii,status="Rejected")



    return render(request,'service/response.html',{'var':var,'var1':var1,'var3':var3,'var4':var4,'var5':var5})

def main_home(request):
    return render(request,'service/main_home.html')

def finish(request):
    ii=request.GET['id']
    var3=Tbl_Request.objects.all().filter(id=ii).update(status="Finished")
    return HttpResponseRedirect('/view_status/')
def finishsss_ride(request):
    ii=request.GET['id']
    var3=Tbl_Request.objects.all().filter(id=ii).update(status="Finished")
    return HttpResponseRedirect('/view_reqst/')

def approve_ride_pass(request):
    ii=request.GET['id']
    chk=Tbl_Request.objects.all().filter(id=ii).update(status="Approved")
    return HttpResponseRedirect('/view_status/')

def approve_ride(request):
    ii=request.GET['id']
    chk=Tbl_Request.objects.all().filter(id=ii).update(status="Approved")
    return HttpResponseRedirect('/view_reqst/')
def join_ride(request):
    if request.method=='POST':

        ii=request.session['id']
        xx=request.POST['iddd']
        start=request.POST["starting"]
        dest=request.POST["ending"]
        cost=request.POST["cost"]
        print("id of current ride is",xx)
        pass_id=user_registration_tb.objects.all().get(id=ii)
        ride_id=VehicleSharing.objects.all().get(id=xx)
        ri_id=VehicleSharing.objects.all().filter(id=xx)
        for x in ri_id:
            driver_id=x.user_id
            print("driver_id objecet",driver_id)
        print("id of passenger ride is",driver_id)
        jo_details=Tbl_Request(driver_id=driver_id,start=start,dest=dest,cost=cost,status="requested",v_id=ride_id,u_id=pass_id)
        jo_details.save()
        return HttpResponseRedirect('/view_status/')
    else:
        idd=request.GET['id']
        print("eeeeeeeee",idd)
        return render(request,'service/join.html',{'idd':idd})
        

def edit_profile(request):
        if request.method=="POST":
            name=request.POST.get("name")
            email=request.POST.get("email")
            phone=request.POST.get("mobile_Number")
            password=request.POST.get("password")
            idd=request.session['id']
            chk=user_registration_tb.objects.all().filter(id=idd).update(password=password,name=name,emailid=email,mobile_Number=phone)
            return HttpResponseRedirect('/view_profile/')
        else:
            ii=request.session['id']
            var=user_registration_tb.objects.all().filter(id=ii)
            for x in var:
                utype=x.user_type

            return render(request,'service/edit_profile.html',{'db':var,'utype':utype})

def edit_ride(request):
        if request.method=="POST":
            ii=request.session['id']
            uid=user_registration_tb.objects.get(id=ii)
            start=request.POST.get("start")
            end=request.POST.get("end")
            cost=request.POST.get("cost")
            date=request.POST.get("date")
            start_time=request.POST.get("start_time")
            # arrival_time=request.POST.get("end_time")
            no_pass=request.POST.get("no_of_pass")
            ride_details=request.POST.get("ride_details")
            gender=request.POST.get("gender")
            vehicle=request.POST.get("vehicle")
            id_of_ride=request.POST['id_of_ride']


            x=VehicleSharing.objects.all().filter(id=id_of_ride).update(user=uid,start=start,dest=end,cost=cost,date=date,start_time=start_time,
            no_pass=no_pass, details=ride_details,gender=gender,status1=vehicle)
            return HttpResponseRedirect('/list_ride/')


        else:
            ii=request.session['id']
            id_of_ride=request.GET['id']
            var=VehicleSharing.objects.all().filter(id=id_of_ride)

            return render(request,'service/edit_ride.html',{'var':var,'id_of_ride':id_of_ride})
           
def users_registration(request):
        if request.method=="POST":
            name=request.POST.get("name")
            email=request.POST.get("email")
            phone=request.POST.get("mobile_Number")
            idproof=request.POST.get("id_proof")
            idno=request.POST.get("id_number")
            password=request.POST.get("password")
            user_type=request.POST.get("user_type")

            chk=user_registration_tb.objects.all().filter(emailid=email)
            if chk:
                return render(request,'service/reg.html')
                # return render(request,'service/reg.html',{'error':'Email Already exists'})

            else:
                a=user_registration_tb(name=name,password=password,emailid=email,mobile_Number=phone,id_proof=idproof,id_number=idno,user_type=user_type)
                a.save()
                return render(request,'service/login.html')
                # return render(request,'service/login.html',{'error':'Email Already exists'})

        else:
            return render(request,'service/reg.html')
            # return render(request,'service/reg.html',{'error':'Email Already exists'})

def users_login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        driver=user_registration_tb.objects.filter(emailid=email,password=password,user_type="Driver")
        Passenger=user_registration_tb.objects.filter(emailid=email,password=password,user_type="Passenger")
        print("ggggggggggggggggggggf",Passenger)

        if driver:
            for x in driver:
                request.session['id']=x.id
            return render(request,'service/index.html')
        
        elif Passenger:
            for x in Passenger:
                request.session['id']=x.id
                print("---------ccccccccccccccccccccc-----------------------------------")

            return render(request,'service/index_pass.html')

        else:
            print("---------ccccccccccccccccccccc-----------------------------------")
            return render(request,'service/login.html')
    else:
        return render(request,'service/login.html')



def index_pass(request):
    return render(request,'service/index_pass.html')

def add_link(request):
    if request.session.has_key('id'):
        if request.method=="POST":

    
            idd = request.POST["idd"]
            from django.core.mail import send_mail
            from django.template.loader import render_to_string
            from django.conf import settings



            linkk=request.POST["linkss"]
            time=request.POST["timee"]
            datee=request.POST["datee"]
            fromform=Tbl_Request.objects.all().filter(id=idd).update(date=datee,
                link=linkk,time=time,status="discussing")
            var=Tbl_Request.objects.all().filter(id=idd)
            for x in var:
                mailid=x.u_id.emailid
            subject = 'Share Your Ride'
            message=render_to_string('service/email_msg.html', {'link': linkk,'time': time,'datee':datee,})            
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [mailid, ] 
            send_mail( subject, message, email_from, recipient_list )

            return HttpResponseRedirect('/view_reqst/')
        else:
            idd=request.GET["id"]
            return render(request,'service/add_link.html',{'idd':idd})



def add_ride(request):
        if request.method=="POST":
            ii=request.session['id']
            uid=user_registration_tb.objects.get(id=ii)
            start=request.POST.get("start")
            end=request.POST.get("end")
            cost=request.POST.get("cost")
            date=request.POST.get("date")
            start_time=request.POST.get("start_time")
            # arrival_time=request.POST.get("end_time")
            no_pass=request.POST.get("no_of_pass")
            ride_details=request.POST.get("ride_details")
            gender=request.POST.get("gender")
            vehicle=request.POST.get("vehicle")


            x=VehicleSharing(user=uid,start=start,dest=end,cost=cost,date=date,start_time=start_time,
            no_pass=no_pass, details=ride_details,gender=gender,status1=vehicle)
            x.save()
            return HttpResponseRedirect('/list_ride/')


        else:
            return render(request,'service/add_ride.html')

def search(request):
        if request.method=="POST":
            vehicle=request.POST.get("vehicle")
            place=request.POST.get("place")
            date=request.POST.get("date")
            place_end=request.POST.get("place_end")

            var=VehicleSharing.objects.all().filter(status1=vehicle,start=place,date=date,dest=place_end)
            print("eeeeeeeeeeeeeeee",var)
            return render(request,'service/result.html',{'var':var})

        else:
            var=VehicleSharing.objects.all()
            return render(request,'service/search.html',{'var':var})

def s_logout(request):
    if request.session.has_key('id'):
        del request.session['id']
        logout(request)
    return HttpResponseRedirect('/main_home/')

def view_feedback(request):
    ii=request.session['id']
    var=Tbl_feedback.objects.all().filter(user=ii)
    return render(request,'service/feed.html',{'var':var})

def logout(request):
    if request.session.has_key('id'):
        del request.session['id']
        logout(request)
    return HttpResponseRedirect('/')