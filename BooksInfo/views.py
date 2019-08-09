from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import book
from .serializers import BookSerializer
from django.http import HttpResponse

class Booklist(APIView):
    def get(self, request):
        book1 = book.objects.all()
        serializer = BookSerializer(book1, many = True)
        return Response(serializer.data)

