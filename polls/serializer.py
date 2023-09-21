from rest_framework.serializers import ModelSerializer
from .models import MoshinaModel

class MoshinaSerializer(ModelSerializer):
    class Meta:
        model = MoshinaModel
        fields=('__all__')