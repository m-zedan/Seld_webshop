from rest_framework import fields, serializers
from .models import HomeAPI, Language, Setting


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAPI
        #fields = ('name','email','subject','date','description')
        fields = ('__all__')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        #fields = ('name','email','subject','date','description')
        fields = ('__all__')
 
class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        #fields = ('name','email','subject','date','description')
        fields = ('__all__')
 