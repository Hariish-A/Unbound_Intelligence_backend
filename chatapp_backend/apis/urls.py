from django.urls import path
from .views import (
    ProviderListCreateView, ProviderDetailView,
    ModelListCreateView, ModelDetailView, SupportedModelsView, ChatCompletionView, FileUploadView
)

urlpatterns = [
    # path("providers/", ProviderListCreateView.as_view(), name="provider-list-create"),
    # path("providers/<int:pk>/", ProviderDetailView.as_view(), name="provider-detail"),
    #
    # path("models/", ModelListCreateView.as_view(), name="model-list-create"),
    # path("models/<int:pk>/", ModelDetailView.as_view(), name="model-detail"),

    path("models/", SupportedModelsView.as_view(), name="supported-models"),
    path('chat/completions/', ChatCompletionView.as_view(), name='chat-completions'),
    path('file/upload', FileUploadView.as_view(), name='file-upload'),

]