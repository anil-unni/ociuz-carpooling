from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ShareApp import views
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from ShareApp import apiapp
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
     path('',views.index),
   
   
    path('login/',views.login),
    path('admin_home/',views.admin_home),
    path('logout/',views.logout),
    path('feedback/',views.feedback),







    # user section
    path('users_registration/',views.users_registration),
    path('users_login/',views.users_login),
    path('search/',views.search),
    path('add_ride/',views.add_ride),
    path('list_ride/',views.list_ride),
    path('all_ride/',views.all_ride),
    path('join_ride/',views.join_ride),
    path('add_link/',views.add_link),

    


    path('s_logout/',views.s_logout),
    path('u_index/',views.u_index),
    path('main_home/',views.main_home),
	path('edit_profile/',views.edit_profile),
    path('view_profile/',views.view_profile),
    path('delete_ride/',views.delete_ride),
    path('view_reqst/',views.view_reqst),
    path('approve_ride/',views.approve_ride),
    path('reject_ride/',views.reject_ride),
    path('view_status/',views.view_status),
    path('main_home/',views.main_home),
    path('index_pass/',views.index_pass),
    path('user_list/',views.user_list),
    path('rate_driver/',views.rate_driver),
    path('edit_ride/',views.edit_ride),
    path('finish/',views.finish),
    path('view_feedback/',views.view_feedback),
    path('approve_ride_pass/',views.approve_ride_pass),
    path('reject_ride_pass/',views.reject_ride_pass),
    path('remove_rideee/',views.remove_rideee),
    path('finishsss_ride/',views.finishsss_ride),
    

    

    


    





   

]