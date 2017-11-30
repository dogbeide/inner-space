from rest_framework import serializers
from models import Tweet, Query

class TweetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tweet
        fields = '__all__'


class QuerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Query
        field = '__all__'
