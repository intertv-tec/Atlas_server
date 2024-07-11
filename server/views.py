from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Automation


def home (request):
    
    return redirect('/admin/')

@csrf_exempt
def register_automation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        automation, created = Automation.objects.get_or_create(name=name)
        return JsonResponse({'success': created})
    return JsonResponse({'error': 'Invalid request method'})

def ping_automation(request, pk,key):
    if request.method == 'GET':
        automation = get_object_or_404(Automation, pk=pk)
        if key == automation.password:
            automation.is_active = True
            automation.last_ping = datetime.now()
            automation.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error':"Invalid Key"})
    return JsonResponse({'error': 'Invalid request method'})
