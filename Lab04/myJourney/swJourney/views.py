from django.shortcuts import render
from .models import LearningEntry, AboutMe  # Import models for database access

# View function for the homepage
def index(request):
    entries = LearningEntry.objects.order_by('-date')[:10]
    return render(request, 'swJourney/index.html', {'entries': entries})

# View function for the About Me page
def about_me(request):
    about = AboutMe.objects.first()
    return render(request, 'swJourney/aboutMe.html', {'about': about})
