from django.db import router
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from imageGram.models import Image
from users.models import Profile
from .serializers import  ImageSerializer, ProfileSerializer



@api_view(['GET'])
def get_links(request):
    endpoints = {
        'all':'/api/',

    }

    return Response(endpoints)

@api_view(['GET'])
def get_images(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def single_image(request, pk):
    try:
        images = Image.objects.get(id=pk)
    except:
        return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ImageSerializer(post)
        return Response(serializer.data)

@api_view(['GET'])
def single_profile(request, pk):
    try:
        profile = Profile.objects.get(id=pk)

    except:
        return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

@api_view(['GET'])
def get_profiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)
