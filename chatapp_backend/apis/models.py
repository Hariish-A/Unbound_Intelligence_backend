from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ChatModel(models.Model):
    model = models.CharField(max_length=255, unique=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='models')

    def __str__(self):
        return f"{self.provider.name}/{self.model}"


class ChatCompletionResponse(models.Model):
    provider = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    prompt = models.TextField()
    response = models.TextField()

    def __str__(self):
        return f"{self.provider} - {self.model}"


class RegexRule(models.Model):
    original_model = models.ForeignKey(ChatModel, related_name='original_rules', on_delete=models.CASCADE)
    regex_pattern = models.CharField(max_length=255)
    redirect_model = models.ForeignKey(ChatModel, related_name='redirect_rules', on_delete=models.CASCADE)

    def __str__(self):
        return f"Rule: {self.original_model} -> {self.redirect_model} (Regex: {self.regex_pattern})"


class FileUploadRule(models.Model):
    file_type = models.CharField(max_length=50, unique=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    model = models.ForeignKey(ChatModel, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.file_type:
            self.file_type = self.file_type.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.file_type} -> {self.provider.name}/{self.model.model}"