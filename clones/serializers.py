from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Event, Category, Item, Post, CustomUser
# from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
    # date = serializers.SerializerMethodField('change_date_format')
    # start_time = serializers.SerializerMethodField('change_start_format')
    # end_time = serializers.SerializerMethodField('change_end_format')
    owner = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    # def change_date_format(self, obj):
    #     return obj.date.strftime("%m-%d-%Y") 

    # def change_start_format(self, obj):
    #     return obj.start_time.strftime("%-l:%M")

    # def change_end_format(self, obj):
    #     return obj.end_time.strftime("%-l:%M")
    
    class Meta:
        model = Event
        fields = '__all__'

    


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    class Meta:
        model = Item
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Post
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'



