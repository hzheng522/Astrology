from django.shortcuts import render
from .forms import BirthChartForm
import requests

def home(request):
    return render(request, 'home.html')

def house(request):
    return render(request, 'house.html')

def planet(request):
    return render(request, 'planet.html')

def sign_view(request):
    signs = [
        {"name": "Aries", "element": "Fire", "date": "Mar 21 - Apr 19", "icon": "aries.png", "description": "Bold, ambitious, fiery."},
        {"name": "Taurus", "element": "Earth", "date": "Apr 20 - May 20", "icon": "taurus.png", "description": "Patient, reliable, grounded."},
        {"name": "Gemini", "element": "Air", "date": "May 21 - Jun 20", "icon": "gemini.png", "description": "Communicative, witty, curious."},
        {"name": "Cancer", "element": "Water", "date": "Jun 21 - Jul 22", "icon": "cancer.png", "description": "Emotional, nurturing, protective."},
        {"name": "Leo", "element": "Fire", "date": "Jul 23 - Aug 22", "icon": "leo.png", "description": "Confident, generous, dramatic."},
        {"name": "Virgo", "element": "Earth", "date": "Aug 23 - Sep 22", "icon": "virgo.png", "description": "Analytical, practical, modest."},
        {"name": "Libra", "element": "Air", "date": "Sep 23 - Oct 22", "icon": "libra.png", "description": "Balanced, sociable, charming."},
        {"name": "Scorpio", "element": "Water", "date": "Oct 23 - Nov 21", "icon": "scorpio.png", "description": "Passionate, resourceful, intense."},
        {"name": "Sagittarius", "element": "Fire", "date": "Nov 22 - Dec 21", "icon": "sagittarius.png", "description": "Adventurous, philosophical, free-spirited."},
        {"name": "Capricorn", "element": "Earth", "date": "Dec 22 - Jan 19", "icon": "capricorn.png", "description": "Disciplined, responsible, determined."},
        {"name": "Aquarius", "element": "Air", "date": "Jan 20 - Feb 18", "icon": "aquarius.png", "description": "Innovative, independent, humanitarian."},
        {"name": "Pisces", "element": "Water", "date": "Feb 19 - Mar 20", "icon": "pisces.png", "description": "Empathetic, artistic, intuitive."}
    ]
    print("🪐 Signs loaded:", signs)
    return render(request, "sign.html", {"signs": signs})

def birth_chart_view(request):
    chart = None
    if request.method == 'POST':
        form = BirthChartForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Call Astrology API
            url = "https://json.astrologyapi.com/v1/western_horoscope"
            user_id = "639878"
            api_key = "96f03ec92d46776d0476ac84cfe7fe29fb638089"

            payload = {
                "name": data['name'] or "Anonymous",
                "birth_date": str(data['birth_date']),
                "birth_time": str(data['birth_time']),
                "latitude": data['latitude'],
                "longitude": data['longitude'],
                "timezone": data['timezone']
            }

            response = requests.post(url, auth=(user_id, api_key), json=payload)
            if response.status_code == 200:
                chart = response.json()
            else:
                chart = {"error": f"API Error {response.status_code}: {response.text}"}
    else:
        form = BirthChartForm()

    return render(request, 'chart.html', {'form': form, 'chart': chart})