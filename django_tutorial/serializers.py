from rest_framework import serializers
from .models import Bear, PicnicBasket, Language, Framework


class PicnicBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = PicnicBasket
        fields = ['id', 'sandwiches', 'bear']

class BearSerializer(serializers.ModelSerializer):
    # picnicbasketbearserializer = PicnicBasketSerializer(many=True, read_only=True)
    class Meta:
        model = Bear
        fields = ['id', 'name', 'age', 'picnicbasketbearserializer']

class FrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Framework
        fields = ['id', 'name', 'language']

class LanguageSerializer(serializers.ModelSerializer):
    framework = FrameworkSerializer(many=True, read_only=True)
    class Meta:
        model = Language
        fields = ['id', 'name', 'framework']

class PicnicBasketBearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bear
        fields = ['id', 'name', 'age']

class PicnicBasketSerializer(serializers.ModelSerializer):
    bear = PicnicBasketBearSerializer(many=False)
    class Meta:
        model = PicnicBasket
        fields = ['id', 'sandwiches', 'bear']
