from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Booking, Menu
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import MenuSerializer

# Create your views here.
def restaurant(request):
    return render(request, 'index.html', {})

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer