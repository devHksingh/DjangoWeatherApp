from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    api_key =os.getenv('RapidAPI-Key')

    url="https://ai-weather-by-meteosource.p.rapidapi.com/current"
    querystring = {"place_id":"Delhi","timezone":"auto","language":"en","units":"metric"}

    headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)

    try:
        api=json.loads(response.content)
    except Exception as e:
        api = "Error........."

    return render(request,'home.html',{'api':api})

def about(request):
    return render(request,'about.html',{})