from django.shortcuts import get_object_or_404
from .models import book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status

class BookList(APIView):
    def get(self, request):
        book1 = book.objects.all()
        serializer = BookSerializer(book1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
