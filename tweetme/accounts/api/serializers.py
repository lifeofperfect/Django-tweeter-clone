from django.contrib.auth.models import User

from rest_framework import serializers

#User = get_user_model

class UserDisplaySerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('username','first_name','last_name','follower_count')
            
            
    def get_follower_count(self, obj):
        return 0