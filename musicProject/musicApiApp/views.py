from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    return render(request, 'index.html')

def search_results(request):
    results = {}
    search_term = request.GET.get('term')
    if search_term:
        url = f'https://itunes.apple.com/search?term={search_term}&media=music&entity=album'
        response = requests.get(url)
        data = response.json()
        # print(data)
        results = data['results']

    context = {
        'results': results
    }
    return render(request, 'search_results.html', context)