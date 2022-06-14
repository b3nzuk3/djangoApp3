from rest_framework.serializers import ModelSerializer
from imageGram.models import Image
from users.models import Profile

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'image' ]
