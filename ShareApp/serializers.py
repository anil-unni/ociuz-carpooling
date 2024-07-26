from rest_framework import serializers
from . models import *

class user_tbSerializer(serializers.ModelSerializer):
	class Meta:
		model=Tbl_User
		fields='__all__'

class route_tbSerializer(serializers.ModelSerializer):
	class Meta:
		model=Tbl_Route
		fields='__all__'

class feedback_tbSerializer(serializers.ModelSerializer):
	class Meta:
		model=Tbl_feedback
		fields='__all__'

class request_tbSerializer(serializers.ModelSerializer):
	class Meta:
		model=Tbl_Request
		fields='__all__'

class vehiclesharing_tbSerializer(serializers.ModelSerializer):
	class Meta:
		model=VehicleSharing
		fields='__all__'
