from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)

def root_view(request):
    return HttpResponse("Welcome to the Simple API. Visit /swagger/ for API documentation.")
