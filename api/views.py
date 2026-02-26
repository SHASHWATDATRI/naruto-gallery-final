from rest_framework import viewsets
from api.models import Artwork
from api.serializers import ArtworkSerializer
from django.http import JsonResponse
from django.contrib.auth.models import User

def fix_admin(request):
    # Purane 'shashwat' user ko delete karke naya banayega
    User.objects.filter(username='shashwat').delete()
    User.objects.create_superuser('shashwat', 'admin@example.com', 'pass123')
    return JsonResponse({"message": "User 'shashwat' created with password 'pass123'"})

class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    