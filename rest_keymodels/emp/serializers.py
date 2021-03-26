from rest_framework import serializers
from .models import Topic, Content


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('name')


class ContentSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=False)

    class Meta:
        model = Content
        fields = ('title', 'body', 'topic')
