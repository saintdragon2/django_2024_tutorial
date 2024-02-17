from django.shortcuts import render


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