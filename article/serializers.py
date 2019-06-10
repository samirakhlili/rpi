from rest_framework import serializers

from article.models import Article, InfoRsp


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

class InforspSerializer(serializers.Serializer):
    temperature = serializers.CharField()
    seaLevel = serializers.CharField()
    time = serializers.CharField()
    date = serializers.CharField()
    serialTag = serializers.CharField()
    position = serializers.CharField()

    def create(self, validated_data):
        return InfoRsp.objects.create(**validated_data)