from django.apps import AppConfig

# Configuration class for the swJourney app
class SwjourneyConfig(AppConfig):
    # Default primary key field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Name of the app as registered in Django
    name = 'swJourney'
