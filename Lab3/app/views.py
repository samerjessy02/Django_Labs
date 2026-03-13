from django.shortcuts import render

# Create your views here.

from app.models import Post, Comment
from rest_framework import serializers
from rest_framework.views import APIView
from django.http import JsonResponse


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'date_posted']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["date_posted"] = instance.date_posted.strftime("%b-%d-%y")
        rep["comments_count"] = Comment.objects.filter(post=instance).count()
        return rep


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)