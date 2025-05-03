import urllib.request
import json
import os
from django.shortcuts import render
from django.conf import settings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def index(request):
    context = {}
    if request.method == 'POST':
        city = request.POST['city']
        
        # Get API key from environment variable
        api_key = os.environ.get('OPENWEATHER_API_KEY')
        
        if not api_key:
            context['error'] = "API key not configured. Please check your environment variables."
            return render(request, "main/index.html", context)
        
        try:
            # Make the API request
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
            source = urllib.request.urlopen(url).read()
            list_of_data = json.loads(source)
            
            # Check if the city was found
            if list_of_data.get('cod') == '404':
                context['error'] = f"City '{city}' not found. Please try another city."
                return render(request, "main/index.html", context)
            
            # Extract weather data
            context = {
                "city_name": city,
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lat']) + ',' + str(list_of_data['coord']['lon']),
                "temp": str(list_of_data['main']['temp']),
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
                'google_maps_api_key': os.environ.get('GOOGLE_MAPS_API_KEY', '')
            }
            
        except Exception as e:
            context['error'] = f"An error occurred: {str(e)}"
    
    return render(request, "main/index.html", context)