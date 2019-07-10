from django.shortcuts import render

# Create your views here.
from leads.models import Lead
from leads.serializers import LeadSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
    

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

#Depreciated due to using custom views class ShowLeadsList(APIView):
'''
class LeadListShow(generics.ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
'''
class ShowLeadsList(APIView):
    def get(self, request):
        leads = Lead.objects.all()[:20]
        data = LeadSerializer(leads, many=True).data
        return Response(data)
