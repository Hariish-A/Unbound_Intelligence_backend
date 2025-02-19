from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import ProviderSerializer, ModelSerializer, ChatCompletionResponseSerializer, FileUploadSerializer

# --- Providers ---
provider_list_schema = swagger_auto_schema(
    operation_summary="List & Create Providers",
    operation_description="Get a list of all providers or create a new provider (Admin only).",
    responses={200: openapi.Response('Success', ProviderSerializer(many=True))}
)

provider_create_schema = swagger_auto_schema(
    operation_summary="Create a Provider",
    operation_description="Create a new provider (Admin only).",
    request_body=ProviderSerializer,
    responses={201: openapi.Response('Success', ProviderSerializer)}
)

provider_detail_schema = swagger_auto_schema(
    operation_summary="Retrieve a Provider",
    operation_description="Retrieve a provider by ID.",
    responses={200: openapi.Response('Success', ProviderSerializer)}
)

provider_update_schema = swagger_auto_schema(
    operation_summary="Update a Provider",
    operation_description="Update a provider (Admin only).",
    request_body=ProviderSerializer,
    responses={200: openapi.Response('Success', ProviderSerializer)}
)

provider_delete_schema = swagger_auto_schema(
    operation_summary="Delete a Provider",
    operation_description="Delete a provider (Admin only).",
    responses={204: "No Content"}
)

# --- Chat Models ---
chat_model_list_schema = swagger_auto_schema(
    operation_summary="List & Create Models",
    operation_description="Get a list of all models or create a new model (Admin only).",
    responses={200: openapi.Response('Success', ModelSerializer(many=True))}
)

chat_model_create_schema = swagger_auto_schema(
    operation_summary="Create a Model",
    operation_description="Create a new model (Admin only).",
    request_body=ModelSerializer,
    responses={201: openapi.Response('Created', ModelSerializer)}
)

chat_model_detail_schema = swagger_auto_schema(
    operation_summary="Retrieve a Model",
    operation_description="Retrieve a model by ID.",
    responses={200: openapi.Response('Success', ModelSerializer)}
)

chat_model_update_schema = swagger_auto_schema(
    operation_summary="Update a Model",
    operation_description="Update a model (Admin only).",
    request_body=ModelSerializer,
    responses={200: openapi.Response('Success', ModelSerializer)}
)

chat_model_delete_schema = swagger_auto_schema(
    operation_summary="Delete a Model",
    operation_description="Delete a model (Admin only).",
    responses={204: "No Content"}
)


supported_models_schema = swagger_auto_schema(
    operation_summary="List Supported Models",
    operation_description="Fetch and return a list of supported models.",
    responses={200: openapi.Response(
        description="A list of supported model names",
        examples={
            "application/json": [
                "openai/gpt-3.5",
                "anthropic/claude-v1",
                "gemini/gemini-alpha"
            ]
        }
    )}
)


chat_completions_schema = swagger_auto_schema(
    operation_summary="Generate Chat Completion",
    operation_description="Route the request to the corresponding stub LLM based on the specified provider and model. "
                          "Static responses for now.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'provider': openapi.Schema(type=openapi.TYPE_STRING),
            'model': openapi.Schema(type=openapi.TYPE_STRING),
            'prompt': openapi.Schema(type=openapi.TYPE_STRING),
        },
        example={
            'provider': 'openai',
            'model': 'gpt-4o',
            'prompt': 'I lost my credit card!',
        }
    ),
    responses={200: openapi.Response('Success', ChatCompletionResponseSerializer)}
)


file_upload_schema = swagger_auto_schema(
        operation_description="Upload a file and get processed response",
        request_body=FileUploadSerializer,
        responses={200: openapi.Response("File successfully processed")},
        manual_parameters=[
            openapi.Parameter(
                name="file",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                description="File to upload"
            )
        ],
)