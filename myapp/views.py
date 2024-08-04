from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MyAPIView(APIView):
    """
    A simple APIView for demonstrating documentation.

    get:
    Returns a list of all items.

    post:
    Creates a new item.
    """

    def get(self, request):
        """
        Retrieve all items.
        """
        items = [{"id": 1, "name": "Item 1"}]
        return Response(items, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new item.
        """
        item = request.data
        return Response(item, status=status.HTTP_201_CREATED)
