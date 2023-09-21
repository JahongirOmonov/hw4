from django.shortcuts import render


from rest_framework.views import APIView
from .serializer import MoshinaSerializer
from rest_framework.response import Response


from .models import MoshinaModel


from django.shortcuts import get_object_or_404


# Create your views here.

class CreateCAR(APIView):
    def post(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            if request.user.roles == 2:


                serialzier = MoshinaSerializer(data=request.data)
                if serialzier.is_valid():
                    serialzier.save()
                    return Response(serialzier.data)
                return Response(serialzier.errors)


        return Response({"msg":"only Matiz cars can add"})
    


    
class UpdateCar(APIView):
    def patch(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            if request.user.roles == 3:


                x= get_object_or_404(MoshinaModel, id=kwargs['forid'])
                serializer=MoshinaSerializer(x, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)


                return Response(serializer.errors)
        return Response("Only Nexia car can change")
    

class ListCar(APIView):
    def get(self, request, *args, **kwargs):

        if str(request.user) != "AnonymousUser":
            print(self.request.user.roles)


            x = MoshinaModel.objects.filter(status=True)
            serializer=MoshinaSerializer(x, many=True)


            return Response(serializer.data)
        return Response({'msg':'Please log in'})