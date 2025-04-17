from django.shortcuts import render
from .forms import BirthChartForm
from django.http import JsonResponse
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

def generate_chart(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        birth_date = request.POST.get('birthDate')
        birth_time = request.POST.get('birthTime')
        location = request.POST.get('location')

        # Fetch latitude, longitude, and time zone using OpenCage Geocoder API
        geocode_api_key = 'ece828a9eae84768b3b3dca6b2107b56'
        geocode_url = f'https://api.opencagedata.com/geocode/v1/json?q={location}&key={geocode_api_key}'
        geocode_response = requests.get(geocode_url).json()

        if geocode_response['results']:
            result = geocode_response['results'][0]
            lat = result['geometry']['lat']
            lon = result['geometry']['lng']
            timezone = result['annotations']['timezone']['offset_sec'] / 3600  # Convert seconds to hours

            # Generate the birth chart using Astrology API
            astrology_api_key = "96f03ec92d46776d0476ac84cfe7fe29fb638089"
            astrology_user_id = "639878"
            astrology_url = "https://json.astrologyapi.com/v1/natal_wheel_chart"
            auth = (astrology_user_id, astrology_api_key)

            data = {
                'day': int(birth_date.split('-')[2]),
                'month': int(birth_date.split('-')[1]),
                'year': int(birth_date.split('-')[0]),
                'hour': int(birth_time.split(':')[0]),
                'min': int(birth_time.split(':')[1]),
                'lat': lat,
                'lon': lon,
                'tzone': timezone,
            }

            astrology_response = requests.post(astrology_url, json=data, auth=auth).json()

            if 'chart_url' in astrology_response:
                return render(request, 'chart_result.html', {'chart_url': astrology_response['chart_url']})
            else:
                return JsonResponse({'error': 'Failed to generate chart.'}, status=500)
        else:
            return JsonResponse({'error': 'Failed to fetch location data.'}, status=400)

    return render(request, 'chart.html')