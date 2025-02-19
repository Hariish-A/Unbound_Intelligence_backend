from django.contrib import admin

from apis.models import Provider, ChatModel, RegexRule, ChatCompletionResponse, FileUploadRule

admin.site.site_header = "ChatApp Admin"
admin.site.site_title = "ChatApp Admin Portal"
admin.site.index_title = "ChatApp Admin Portal"

admin.site.register(Provider)
admin.site.register(ChatModel)
admin.site.register(RegexRule)
admin.site.register(ChatCompletionResponse)
admin.site.register(FileUploadRule)