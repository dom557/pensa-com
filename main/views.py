import json
from django.shortcuts import render
from django.conf import settings
import os


def home(request):
    # Load the JSON data
    json_file_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'data', 'members.json')
    with open(json_file_path, 'r') as f:
        members = json.load(f)
    
    return render(request, 'home.html', {'members': members})


def search(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    
    results = []
    if query:
        # Load the JSON data
        json_file_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'data', 'members.json')
        with open(json_file_path, 'r') as f:
            members = json.load(f)
        
        # Filter members based on the search query
        for member in members:
            if query.lower() in member['name'].lower() or query.lower() in member['role'].lower():
                results.append(member)
    
    return render(request, 'home.html', {'query': query, 'results': results})
