from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Entry
from .serializers import EntrySerializer

class EntryApiView(APIView):

    permission_classes = []

    def get(self, request, *args, **kwargs):
        entries = Entry.objects.all().order_by('-created_at')
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'nickname': request.data.get('nickname'), 
            'email': request.data.get('email'), 
            'message': request.data.get('message')
        }
        serializer = EntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)