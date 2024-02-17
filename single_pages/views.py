from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(
        request, 
        'single_pages/index.html'
    )
    
def about(request):
    return render(
        request, 
        'single_pages/about.html', 
        {
            'greeting': 'Hello, World!',
            'numbers': [1, 2, 3, 4, 5]
        }
    )
       
def http_response_practice(request):
    return HttpResponse('Hello, World! This is a practice of HttpResponse.')

def json_response_practice(request):
    return JsonResponse({
        'message': 'Hello, World! This is a practice of JsonResponse.',
        'numbers': [1, 2, 3, 4, 5]
    })