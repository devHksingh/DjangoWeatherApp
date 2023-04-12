from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    api_key =os.getenv('RapidAPI-Key')
    url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q=New Delhi&days=3&aqi=no&alerts=yes"
    
    api_request= requests.get(url)
    # print(response)

    try:
        api=json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request,'home.html',{'api':api})

def about(request):
    return render(request,'about.html',{})