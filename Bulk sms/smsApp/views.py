from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .sms_service import send_sms

def send_notification(request):
    if request.method == 'POST':
        recipients = request.POST.get('recipients').split(',')
        message = request.POST.get('message')
        response = send_sms(recipients, message)
        if response:
            return JsonResponse({'status': 'success', 'response': response})
        else:
            return JsonResponse({'status': 'error', 'message': 'Failed to send SMS'})
    return render(request, 'send_notification.html')
