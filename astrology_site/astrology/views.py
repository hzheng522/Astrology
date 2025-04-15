from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def house(request):
    return render(request, 'house.html')

def planet(request):
    return render(request, 'planet.html')

def chart(request):
    return render(request, 'chart.html')

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
