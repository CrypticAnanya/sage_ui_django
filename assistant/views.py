from django.shortcuts import render
from django.http import JsonResponse
from .sage import get_reply
import os 
import json
from django.http import JsonResponse

def process_voice(request):
    if request.method == "POST":
        data = json.loads(request.body)
        command = data.get("command", "").lower()

        # Process command
        if "open notepad" in command:
            os.system("notepad")
        elif "open chrome" in command:
            os.system("start chrome")
        # Add more commands here

        return JsonResponse({"status": "success", "command": command})

def home(request):
    return render(request, 'assistant/index.html')

def ask_sage(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        reply = get_reply(message)
        return JsonResponse({'reply': reply})
