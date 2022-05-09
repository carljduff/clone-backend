from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import EventSerializer, CategorySerializer, ItemSerializer, PostSerializer, PhotoSerializer, CustomUserSerializer
from .models import Event, Category, Item, Post, Photo, CustomUser
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

# class EventViewSet(viewsets.ModelViewSet):
    # queryset = Event.objects.all()
    # serializer_class = EventSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['owner']
    # search_fields = ['=title', 'description']

class EventViewSet(viewsets.ModelViewSet):
    # queryset = Event.objects.all()

    serializer_class = EventSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ['owner']
    ordering_fields = ['id']
    ordering = ['id']
    # search_fields = ['=title', 'description']
    # queryset = Event.objects.all()
    
    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(owner=user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
   
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filterset_fields = ['event__id']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
