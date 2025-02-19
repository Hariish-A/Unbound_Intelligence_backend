from rest_framework import generics
from rest_framework.response import Response

from .adapter import OpenAIAdapter, AnthropicAdapter, GeminiAdapter, OpenAIFileAdapter, AnthropicFileAdapter, GeminiFileAdapter
from .models import Provider, ChatModel, ChatCompletionResponse, FileUploadRule
from .serializers import ProviderSerializer, ModelSerializer, ChatCompletionResponseSerializer, FileUploadSerializer
from .permissions import AdminOnlyEditPermission
from .swagger_schemas import (
    provider_list_schema, provider_create_schema, provider_detail_schema, provider_update_schema,
    provider_delete_schema,
    chat_model_list_schema, chat_model_create_schema, chat_model_detail_schema, chat_model_update_schema,
    chat_model_delete_schema,
    supported_models_schema, chat_completions_schema, file_upload_schema
)
from rest_framework.permissions import AllowAny

from .utils import check_and_redirect
from django.shortcuts import get_object_or_404
import magic
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser


class ProviderListCreateView(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [AdminOnlyEditPermission]

    @provider_list_schema
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @provider_create_schema
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [AdminOnlyEditPermission]

    @provider_detail_schema
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @provider_update_schema
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @provider_delete_schema
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ModelListCreateView(generics.ListCreateAPIView):
    queryset = ChatModel.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [AdminOnlyEditPermission]

    @chat_model_list_schema
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @chat_model_create_schema
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatModel.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [AdminOnlyEditPermission]

    @chat_model_detail_schema
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @chat_model_update_schema
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @chat_model_delete_schema
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SupportedModelsView(generics.ListAPIView):
    """
    Fetches and returns the list of supported models.
    """
    queryset = ChatModel.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [AllowAny]

    @supported_models_schema
    def get(self, request, *args, **kwargs):
        models = [f"{model.provider.name}/{model.model}" for model in ChatModel.objects.all()]

        return Response(models)


class ChatCompletionView(generics.CreateAPIView):
    """
    Handles generating chat completions based on the provider and model.
    """
    permission_classes = [AllowAny]
    serializer_class = ChatCompletionResponseSerializer

    @chat_completions_schema
    def post(self, request, *args, **kwargs):
        # Extract request data
        provider_name = request.data.get("provider")
        model_name = request.data.get("model")
        prompt = request.data.get("prompt")

        # Retrieve the Provider object (get_or_404 will raise a 404 error if not found)
        provider = get_object_or_404(Provider, name=provider_name)

        # Check and reroute if necessary based on regex
        provider_model = get_object_or_404(ChatModel, provider=provider, model=model_name)

        # Retrieve the ChatModel object by name and provider
        redirected_model = check_and_redirect(prompt, provider, provider_model)

        redirected_provider = redirected_model.provider

        # Select the appropriate adapter based on the redirected model's provider
        if redirected_provider.name == "openai":
            adapter = OpenAIAdapter()
        elif redirected_provider.name == "anthropic":
            adapter = AnthropicAdapter()
        elif redirected_provider.name == "gemini":
            adapter = GeminiAdapter()
        else:
            return Response({"error": "Invalid provider"}, status=400)

        # Generate the response using the adapter
        response_text = adapter.generate_response(redirected_model, prompt)

        # Store the response in the database
        # chat_response = ChatCompletionResponse.objects.create(
        #     provider=redirected_provider,
        #     model=redirected_model,
        #     prompt=prompt,
        #     response=response_text
        # )

        # Return the stored response using the serializer
        # return Response(ChatCompletionResponseSerializer(chat_response).data)

        response_data = {
            "provider": redirected_provider.name,  # Use the redirected provider name
            "model": redirected_model.model,  # Use the redirected model name
            "response": response_text
        }

        # Return the response data using the serializer (without saving to the DB)
        return Response(response_data)


class FileUploadView(APIView):
    """
    Handles file uploads and routes to the appropriate model for processing.
    """
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    @file_upload_schema
    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            return Response({"error": "No file uploaded"}, status=400)

        # Detect file type using magic (MIME type)
        mime = magic.Magic(mime=True)
        file_type = mime.from_buffer(uploaded_file.read(2048)).split('/')[1].upper()

        # Find the corresponding rule
        file_rule = get_object_or_404(FileUploadRule, file_type=file_type)

        # Get the corresponding provider and model
        provider = file_rule.provider
        model = file_rule.model

        # Select the correct adapter
        if provider.name == "openai":
            adapter = OpenAIFileAdapter()
        elif provider.name == "anthropic":
            adapter = AnthropicFileAdapter()
        elif provider.name == "gemini":
            adapter = GeminiFileAdapter()
        else:
            return Response({"error": "Invalid provider"}, status=400)

        # Process the file
        response_text = adapter.process_file(uploaded_file, model)

        # Return the response
        response_data = {
            "provider": provider.name,
            "model": model.model,
            "response": response_text
        }
        return Response(response_data)