from rest_framework.serializers import ModelSerializer
from enrolls.models import *

class EnrollSerializer(ModelSerializer):

    class Meta:
        model = Enroll
        fields = '__all__'

        