from rest_framework import serializers
from .models import Bear, PicnicBasket, Language, Framework


class PicnicBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = PicnicBasket
        fields = ['id', 'sandwiches', 'bear']

class BearSerializer(serializers.ModelSerializer):
    picnicbaskets = PicnicBasketSerializer(many=True, read_only=True)
    class Meta:
        model = Bear
        fields = ['id', 'name', 'age', 'picnicbaskets']

class FrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Framework
        fields = ['id', 'name', 'language']

class LanguageSerializer(serializers.ModelSerializer):
    framework = FrameworkSerializer(many=True, read_only=True)
    class Meta:
        model = Language
        fields = ['id', 'name', 'framework']
