from django.http import JsonResponse
import json

# Create your views here.
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from chatbot.Robot import Chatbot

@method_decorator(csrf_exempt, name='dispatch')
class ChatView(View):
    chatbot = None
    def get(self, request):
        if ChatView.chatbot == None:
            ChatView.chatbot = Chatbot()
        return render(request, 'chatbot.html')
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))  # 解析请求体
        message = data['message']  # 从JSON数据中获取'message'
        if ChatView.chatbot:
            # 调用chatbot并返回响应
            response = ChatView.chatbot.ask(message)
            return JsonResponse({'message': response})
        return JsonResponse({'message': 'No chatBot!'})