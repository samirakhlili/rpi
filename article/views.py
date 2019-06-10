from rest_framework.response import Response
from rest_framework.views import APIView

from article.serializers import ArticleSerializer, InforspSerializer
from .models import Article,InfoRsp

class InfoRspView(APIView):

    def get(self, request):
        infoRsp = InfoRsp.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = InforspSerializer(infoRsp, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get('article')

        # Create an article from the above data
        serializer = InforspSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            info_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(info_saved.time)})

class ArticleView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get('article')

        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})
