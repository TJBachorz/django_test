from django.shortcuts import render
from rest_framework import viewsets
from .models import Bear, PicnicBasket, Language, Framework
from .serializers import BearSerializer, PicnicBasketSerializer, LanguageSerializer, FrameworkSerializer

# Create your views here.

class BearView(viewsets.ModelViewSet):
    queryset = Bear.objects.all()
    serializer_class = BearSerializer
    
class PicnicBasketView(viewsets.ModelViewSet):
    queryset = PicnicBasket.objects.all()
    serializer_class = PicnicBasketSerializer
    
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    
class FrameworkView(viewsets.ModelViewSet):
    queryset = Framework.objects.all()
    serializer_class = FrameworkSerializer
    


