# Weather Dashboard App

![Weather App Screenshot](/api/placeholder/800/400 "Weather App Screenshot")

A beautiful, responsive weather application built with Django and OpenWeatherMap API. Get real-time weather information for any city in the world, including temperature, humidity, pressure, and more - all displayed on an interactive map.

## Features

- 🔍 **Search by City Name**: Get weather information for any city worldwide
- 🌡️ **Real-Time Weather Data**: Temperature, pressure, humidity, and weather conditions
- 🗺️ **Interactive Map**: Visualize the exact location using Google Maps integration
- 📱 **Responsive Design**: Works perfectly on both desktop and mobile devices
- 🎨 **Modern UI**: Beautiful, intuitive interface with smooth animations
- 🛡️ **Secure API Handling**: Environment-based API key management for security

## Tech Stack

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, CSS, Bootstrap 4, JavaScript
- **APIs**: OpenWeatherMap API, Google Maps API
- **Data Format**: JSON
- **Styling**: Custom CSS with Bootstrap Flatly theme
- **Icons**: Font Awesome 5

## Installation and Setup

### Prerequisites

- Python 3.6+
- Django 3.0+
- An OpenWeatherMap API key
- A Google Maps API key (optional, for map functionality)

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/weather-dashboard.git
cd weather-dashboard
```

### Step 2: Set up a virtual environment

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows
env\Scripts\activate
# On macOS/Linux
source env/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set up environment variables

Create a `.env` file in the project root directory:

```
# API Keys
OPENWEATHER_API_KEY=your_openweather_api_key_here
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here

# Django settings
SECRET_KEY=your_django_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Step 5: Apply migrations

```bash
python manage.py migrate
```

### Step 6: Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the application.

## How to Use

1. Enter a city name in the search box
2. Click "Search" or press Enter
3. View the weather information and location on the map
4. Search for another city to compare weather conditions

## API Keys

### OpenWeatherMap API

This application uses the OpenWeatherMap API to fetch weather data. To get an API key:

1. Sign up at [OpenWeatherMap](https://openweathermap.org/)
2. Generate an API key from your account dashboard
3. Add the key to your `.env` file

### Google Maps API

For the map functionality, you'll need a Google Maps JavaScript API key:

1. Sign up for a Google Cloud Platform account
2. Create a new project
3. Enable the Maps JavaScript API
4. Create an API key with appropriate restrictions
5. Add the key to your `.env` file

## Project Structure

```
weather-dashboard/
├── manage.py
├── .env                  # Environment variables (not in repository)
├── .env.example          # Example environment file
├── .gitignore            # Git ignore file
├── README.md             # This file
├── requirements.txt      # Python dependencies
├── weather_project/      # Main Django project folder
│   ├── __init__.py
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL configurations
│   ├── asgi.py
│   └── wsgi.py
└── weather_app/          # Weather application
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py           # App-specific URLs
    ├── views.py          # View functions
    └── templates/        # HTML templates
        └── main/
            └── index.html  # Main template file
```
