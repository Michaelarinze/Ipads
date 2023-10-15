from django.http import JsonResponse
from .models import Ipad
from .serializers import Ipadserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view (['GET','POST'])

def ipadlist (request):
    if request.method == 'GET' :
      ipad = Ipad.objects.all()
      serializer = Ipadserializer(ipad, many=True)
      return JsonResponse({'ipads':serializer.data})

    if request.method  == 'POST':
      serializer= Ipadserializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view ( ['GET','PUT','DELETE'] )  
def ipadetail(request,id):
   try:
      ipad=Ipad.objects.get(pk=id)
   except Ipad.DoesNotExist :
      return Response(status.HTTP_404_NOT_FOUND)
   
   if request.method =="GET":
      serializer = Ipadserializer(ipad)
      return Response(serializer.data)
   
   elif request.method == 'PUT':
      serializer = Ipadserializer(ipad,data = request.data)
      if serializer.is_valid:
         serializer.save
         return Response(serializer.data)
      return Response(serializer.errors ,status= status.HTTP_204_NO_CONTENT)
   
   elif request.data == 'DELETE':
      ipad.delete
      return Response(status=status.HTTP_401_UNAUTHORIZED)
