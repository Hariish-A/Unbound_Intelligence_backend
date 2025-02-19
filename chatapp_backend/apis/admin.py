from django.contrib import admin

from apis.models import Provider, ChatModel, RegexRule, ChatCompletionResponse

admin.site.site_header = "ChatApp Admin"
admin.site.site_title = "ChatApp Admin Portal"
admin.site.index_title = "Welcome to ChatApp Portal"

admin.site.register(Provider)
admin.site.register(ChatModel)
admin.site.register(RegexRule)
admin.site.register(ChatCompletionResponse)