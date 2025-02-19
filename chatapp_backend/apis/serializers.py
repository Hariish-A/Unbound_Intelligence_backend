from rest_framework import serializers

from apis.models import Provider, ChatModel, ChatCompletionResponse


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name']


class ModelSerializer(serializers.ModelSerializer):
    provider = serializers.StringRelatedField()

    class Meta:
        model = ChatModel
        fields = ['id', 'model', 'provider']


class ChatCompletionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatCompletionResponse
        fields = ['provider', 'model', 'response']